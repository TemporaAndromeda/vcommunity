from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Post, Comment, Tag
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def post(request):
    projects = Post.objects.all()
    context={'post': projects}
    return render(request, 'community/posts.html', context)
    
@login_required(login_url="login")
def posts(request, pk):
    projectObj = Post.objects.get(id = pk)
    return render(request, 'community/single-posts.html',  {"posts": projectObj})

@login_required(login_url="login")
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post")
    
    context={'form': form}
    return render(request, "community/post_form.html", context)


@login_required(login_url="login")
def updatePost(request,pk):
    project = Post.objects.get(id = pk)
    form = PostForm(instance = project)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('post')
    
    context={'form': form}
    return render(request, "community/post_form.html", context)


@login_required(login_url="login")
def deletePost(request, pk):
    project = Post.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('post')
    context = {"object": project}
    return render(request, 'community/delete_object.html', context)

