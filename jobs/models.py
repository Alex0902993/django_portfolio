from django.db import models

# Create your models here.

# Job model
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)


# Blog model
class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.TextField()