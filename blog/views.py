from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    msg = "You are on the Blog Page"
    return render(request, 'blog/blog.html', {"message": msg})

# Create your views here.
