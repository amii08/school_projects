from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .forms import TagForm, PostForm
from django.urls import reverse
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.all()

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    return render(request, 'forum/index.html', context={'posts': posts})



class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'forum/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'forum/post_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'forum/post_update_form.html'

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'forum/post_delete_form.html'
    redirect_url = 'post_list_url'


class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'forum/tag_detail.html'

class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'forum/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'forum/tag_update_form.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag 
    template = 'forum/tag_delete_form.html'
    redirect_url = 'tags_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'forum/tags_list.html', context={'tags': tags})
