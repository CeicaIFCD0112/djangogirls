from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    return render(request,'blog/blog_intro.html',{})

def proyectos(request):
    return render(request,'blog/proyectos.html',{})
