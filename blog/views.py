from django.shortcuts import render
from .models import *

# Create your views here.
def blog(request):
    posts_intro = Posts.objects.all()
    blog_dic = {'posts_intro': posts_intro}

    return render(request, "blog/blog.html", blog_dic)


def posts(request,slug):
    post = Posts.objects.get(slug=slug)

    return render(request, 'blog/posts.html', {'post':post,})
