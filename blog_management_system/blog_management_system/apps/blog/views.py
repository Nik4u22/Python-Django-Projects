from django.shortcuts import render
from django.http import HttpResponse
from apps.blog.models import Post, Category

# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]
    categories = Category.objects.all()
    data = {
        'posts': posts,
        'categories': categories
    }
    return render(request, "home.html", data)

def post(request, url):
    #Post.objects.filter(url=url)
    post = Post.objects.get(url=url)
    return render(request, 'posts.html', {'post': post})
    