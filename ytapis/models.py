from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    thumbnail = models.CharField(max_length=500, blank=True, null=True)
