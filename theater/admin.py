from django.contrib import admin
from .models import Media, Tag, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created',)
