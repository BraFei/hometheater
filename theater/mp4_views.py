from django.shortcuts import render, get_object_or_404
from .models import Media, Category, Tag


def mp4_index(req):
    content = dict()
    MP4s = Media.objects.filter(type_in_media='MP4')
    content['MP4s'] = MP4s
    return render(req, 'theater/mp4_index.html', content)


def mp4_details(req, mp4_id):
    content = dict()
    MP4 = get_object_or_404(Media, id=mp4_id)
    content['MP4'] = MP4
    content['tags'] = MP4.tag.all()
    content['next'] = Media.objects.filter(type_in_media='MP4').filter(id__gt=MP4.id).first()
    content['pre'] = Media.objects.filter(type_in_media='MP4').filter(id__lt=MP4.id).last()
    return render(req, 'theater/mp4_details.html', content)


def mp4_same_tags(req, tag_id):
    content = dict()
    tag = get_object_or_404(Tag, id=tag_id)
    content['MP4s'] = Media.objects.filter(tag=tag).filter(type_in_media='MP4')
    return render(req, 'theater/mp4_index.html', content)


def mp4_insert(req):
    pass