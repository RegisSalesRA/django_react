from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=150)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=options,default='published')

    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title

class YouTubeSchedule(models.Model):
    timetamp = models.DateTimeField(auto_now_add=True)        
    updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title