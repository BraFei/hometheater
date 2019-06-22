from django.db import models
from django.utils import timezone
from read_statistics.models import ReadNumExpandMethod

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Media(models.Model, ReadNumExpandMethod):
    MP3 = 'MP3'
    MP4 = 'MP4'
    FILE = 'FILE'
    IMG = 'IMG'
    TYPE_IN_MEDIA_CHOICES = (
        (MP3, 'mp3'),
        (MP4, 'mp4'),
        (FILE, 'file'),
        (IMG, 'img'),
    )
    title = models.CharField(max_length=20)
    type_in_media = models.CharField(max_length=4,  choices=TYPE_IN_MEDIA_CHOICES,  default=MP4)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag)
    context = models.TextField(null=True, blank=True)
    media_file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Media: %s>" % self.title
