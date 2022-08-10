from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page


@cache_page(5, key_prefix='index_page')
def index(request):
    post_list = Post.objects.select_related('author', 'category').order_by('-pub_date')

    return render(
        request,
        "index.html",
        {"posts": post_list}
    )
