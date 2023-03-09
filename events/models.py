from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self) :
        return self.title
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='albums')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_photos')
    image = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

