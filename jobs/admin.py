from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Blog

admin.site.register(Job)

admin.site.register(Blog)