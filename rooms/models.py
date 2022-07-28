import uuid
from django.conf import settings
from django.db import models
from users.models import Profile

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(Profile, null=True, blank= True, on_delete=models.SET_NULL) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(Profile, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable= False)

    class Meta:
        ordering =['-updated', '-created']

    def __str__(self):
        return self.name


class Replies(models.Model):
    user = models.ForeignKey(Profile, null=True, blank= True, on_delete=models.SET_NULL) 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable= False)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering =['-updated', '-created']