from django.db import models
from django.utils import timezone

# Create your models here.

# Job model
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)


# Blog model
class Blog(models.Model):
    title = models.CharField(default="", max_length=255)
    pubdate = models.DateTimeField(default=timezone.now)
    body = models.TextField(default="")
    image = models.ImageField(upload_to="images/")