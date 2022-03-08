from rest_framework import serializers
from core.models import Category, Post

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