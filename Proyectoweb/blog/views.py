from django.shortcuts import render, HttpResponse
from blog.models import Categoria, Post

# Create your views here.


def blog(request):

    post=Post.objects.all()

    return render(request, "blog/blog.html", {"post": post})