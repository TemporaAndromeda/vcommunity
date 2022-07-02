from django.urls import path
from . import views

urlpatterns =[

path('post/', views.post, name="post"),
path('posts/<str:pk>/', views.posts, name="posts"),
path('create-post/', views.createPost, name="create-post"),
path('update-post/<str:pk>/', views.updatePost, name= 'update-post'),
path('delete-post/<str:pk>/', views.deletePost, name= 'delete-post'),
]