from django import template
from Blog.models import *

register = template.Library()


@register.inclusion_tag('inc/_popular_posts.html', )
def show_popular_posts(cnt=3):
    posts = Post.objects.order_by("-views")[:cnt]
    return {'posts': posts}


@register.inclusion_tag('inc/_tags_list.html', )
def show_tags_list():
    tags = Tage.objects.all()
    return {'tags': tags}


@register.inclusion_tag('inc/_search.html', )
def show_search_ponel():
    return
