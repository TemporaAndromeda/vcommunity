from tkinter import CASCADE
import uuid
from django.conf import settings
from django.db import models
from users.models import Profile

# Create your models here.

class Tag(models.Model):
    name =models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable= False)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(Profile, null=True, blank= True, on_delete=models.SET_NULL)
    VOTE_TYPE_POSTS = ((+1, 'UP VOTE'), (-1, ("DOWN VOTE")))
    Report_TYPE_POSTS = ((+1, 'Reported'),(0, 'Report'))
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable= False)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=4000, editable=True, blank=True)
    post_image= models.ImageField(blank = True, null=True, default ="default.jpg")
    source_link = models.CharField(max_length=2000, null=True, blank= True)
    tags = models.ManyToManyField(Tag, blank= True)
    number_of_comments = models.IntegerField(default = 0, editable = False)
    report_value = models.IntegerField(default=0, choices=Report_TYPE_POSTS)
    report_total = models.IntegerField(default=0, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_Ratio = models.IntegerField(default=0, null=True, blank=True)
    vote_value = models.IntegerField(default=0, choices=VOTE_TYPE_POSTS)
    creator_name = models.CharField(max_length = 200,editable= False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    VOTE_TYPE_COMMENTS = ((+1, 'UP VOTE'), (-1, ("DOWN VOTE")))
    Report_TYPE_COMMENTS = ((+1, 'Reported'), (0, "Report"))
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable= False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    sdescription = models.TextField(max_length=4000, editable=True, blank=True)
    com_image= models.ImageField(blank=True)
    report_value = models.IntegerField(default=0, choices=Report_TYPE_COMMENTS)
    vote_value = models.IntegerField(default=0, choices=VOTE_TYPE_COMMENTS)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    creator_name = models.CharField(max_length = 200, editable= False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
        
