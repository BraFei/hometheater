from django.shortcuts import render, get_object_or_404
from .models import Media, Category, Tag
from django.http import FileResponse


# Create your views here.
def index(req):
    content = dict()
    # content['hello'] = 'world'
    MP4s = Media.objects.filter(type_in_media='MP4')
    content['MP4s'] = MP4s
    return render(req, 'theater/index.html', content)


def download(req):
    file = open("static/xlsx/test.xlsx", 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-disposition'] = 'attachment; filename = "test.xlsx"'
    return response

