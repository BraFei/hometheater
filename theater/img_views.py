from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Media, Category, Tag
from read_statistics.utils import read_statistics_once_read
from django.core.paginator import Paginator
from django.conf import settings


def get_paginator_list_common_data(req, content_list):
    paginator = Paginator(content_list, settings.EACH_PAGE_OF_NUMBER)
    page_num = req.GET.get('page', 1)  # 获取url的页面参数（GET请求）
    page_of_content = paginator.get_page(page_num)
    current_page_num = page_of_content.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = dict()
    context['content'] = page_of_content.object_list  # 获取这一页有多少个内容，结果是一个类似于列表
    context['page_of_content'] = page_of_content
    context['page_range'] = page_range
    return context


def img_index(req):
    content = dict()
    images = Media.objects.filter(type_in_media='IMG')
    context = get_paginator_list_common_data(req, images)
    content['page_range'] = context['page_range']
    content['page_of_images'] = context['page_of_content']
    content['images'] = context['content']
    return render(req, 'theater/img_index.html', content)


def img_details(req, img_id):
    content = dict()
    img = get_object_or_404(Media, id=img_id)
    read_cookie_key = read_statistics_once_read(req, img)
    content['img'] = img
    content['tags'] = img.tag.all()
    response = render_to_response('theater/img_details.html', content)
    response.set_cookie(read_cookie_key, 'true')
    return response


def img_same_tags(req, tag_id):
    content = dict()
    tag = get_object_or_404(Tag, id=tag_id)
    content['imgs'] = Media.objects.filter(tag=tag).filter(type_in_media='IMG')
    return render(req, 'theater/img_index.html', content)
