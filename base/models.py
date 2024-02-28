from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)  # room can only have one topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # means this column can be blank. null = True is for database and blank = True is for form
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)  # whenever we press save button, this will automatically update date and time
    created = models.DateTimeField(auto_now_add=True)  # will only update once, that is the first time we press the save button
    video = models.FileField(upload_to='', null=True, blank=True)  # Directory where video files will be stored
    pdf = models.FileField(upload_to='', null=True, blank=True)  # Directory where PDF files will be stored


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)#when a room is deleted, all the message will be deleted automatically using this cascade function
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
