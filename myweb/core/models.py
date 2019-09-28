from django.db import models
from django.urls import reverse

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)#title
    description = models.CharField(max_length=500, null= True)#New
    tags = models.CharField(max_length=50, null= True)#New
    categories = models.CharField(max_length=20, null= True)#New
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    video = models.FileField(upload_to='')
    cover = models.ImageField(upload_to='', null= True, blank=True)
    duration = models.FloatField(null= True)

    def __str__(self):
        return self.title