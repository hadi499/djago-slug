from django.shortcuts import render , get_object_or_404
from .models import Post
from django.contrib.auth.models import User

def home(request):
    posts = Post.post_publish.all()   
    return render(request, 'home.html', {'posts': posts})

def detail(request, post):
    post = get_object_or_404(Post, slug=post, status='publish')
    return render(request, 'detail.html', {'post': post})