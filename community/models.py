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
    VOTE_TYPE_POSTS = (('up', 'UP VOTE'), ('down', ("DOWN VOTE")))
    Report_TYPE_POSTS = (('up', 'Reported'),('down', 'Report'))
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
    vote_value = models.IntegerField(default='up', choices=VOTE_TYPE_POSTS)
    creator_name = models.CharField(max_length = 200,editable= False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_Ratio','-vote_total', 'title']

    @property
    def reviewers(self):
        queryset = self.comment_set.all().values_list('owner__id', flat=True)
        return queryset
    
    @property
    def getVoteCount(self):
        reviews = self.comment_set.all()
        upvotes = reviews.filter(vote_value='up').count()
        totalVotes = reviews.count()

        ratio = (upvotes/totalVotes)*100
        self.vote_total = totalVotes
        self.vote_Ratio = ratio
        self.save()

class Comment(models.Model):
    VOTE_TYPE_COMMENTS = (('up', 'UP VOTE'), ('up', ("DOWN VOTE")))
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable= False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField(max_length=4000, editable=True, blank=True)
    vote_value = models.CharField(max_length=200, choices=VOTE_TYPE_COMMENTS)
    creator_name = models.CharField(max_length = 200, editable= False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vote_value

        
