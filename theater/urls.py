from django.urls import path
from .views import *
from .mp4_views import *
from .img_views import *
urlpatterns = [
    path('', index, name='index'),
    path('mp4/', mp4_index, name='mp4_index'),
    path('mp4_details/<int:mp4_id>', mp4_details, name='mp4_details'),
    path('img/', img_index, name='img_index'),
    path('img_details/<int:img_id>', img_details, name='img_details'),
    path('mp4_same_tags/<int:tag_id>', mp4_same_tags, name='mp4_same_tags'),
    path('img_same_tags/<int:tag_id>', img_same_tags, name='img_same_tags'),
    path('download/', download, name='download'),
]
