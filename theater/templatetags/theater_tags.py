from django import template
register = template.Library()
from ..models import *


@register.simple_tag
def get_mp4_with_tags():
    return Media.objects.dates('month', order='DESC')
