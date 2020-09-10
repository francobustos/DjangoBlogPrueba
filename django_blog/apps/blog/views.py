from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def generals(request):
    return render(request, 'generals.html')

def anime(request):
    return render(request, 'anime.html')

def piano(request):
    return render(request, 'piano.html')

def literature(request):
    return render(request, 'literature.html')
