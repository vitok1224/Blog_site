from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('categories/<str:slug>', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>', GetPostDetail.as_view(), name='post'),
    path('tage/<str:slug>', TageByPost.as_view(), name='tage'),
    path('search', SearchPosts.as_view(), name='search')
]
