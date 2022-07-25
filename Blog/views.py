from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import *


class Home(ListView):
    model = Post
    template_name = 'Blog/Home.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class PostsByCategory(ListView):
    template_name = 'Blog/Home.html'
    paginate_by = 4
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetPostDetail(DetailView):
    model = Post
    template_name = 'Blog/PostDetail.html'
    paginate_by = 4
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class TageByPost(ListView):
    template_name = 'Blog/Home.html'
    paginate_by = 4
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tage__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "News from tag: " + str(Tage.objects.get(slug=self.kwargs['slug']))
        return context


class SearchPosts(ListView):
    template_name = 'Blog/Search.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Search"
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
