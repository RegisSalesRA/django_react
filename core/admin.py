from django.contrib import admin
from core.models import Post,Category, YouTubeSchedule

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(YouTubeSchedule)