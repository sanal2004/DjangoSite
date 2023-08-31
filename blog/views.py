from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
    # posts = Article.objects.all()
    posts = Article.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def test(request):
    return HttpResponse('<h1> Test page </h1>')

def wel(request):
    return HttpResponse('<h1> Welcome </h1>')
