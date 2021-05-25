from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
