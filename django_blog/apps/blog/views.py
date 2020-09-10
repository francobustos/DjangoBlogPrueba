from django.shortcuts import render
from .models import Post, Category

def home(request):
    posts = Post.objects.filter(state = True)
    return render(request, 'index.html',{'posts':posts})

def detailsPost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    return render(request, 'post.html', {'details_post': post})

def generals(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'General')
    )
    return render(request, 'generals.html',{'posts':posts})

def anime(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Anime')
    )
    return render(request, 'anime.html',{'posts':posts})

def piano(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Piano')
    )
    return render(request, 'piano.html',{'posts':posts})

def literature(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Literatura')
    )
    return render(request, 'literature.html',{'posts':posts})
