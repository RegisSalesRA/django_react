from rest_framework import serializers
from core.models import Category, Post, YouTubeSchedule

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
        'category',
        'content',
        'title',
        'author',
        'status']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
        'name']

class YouTubeScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeSchedule
        fields = ['id',
        'title',
        'description',
        'completed']