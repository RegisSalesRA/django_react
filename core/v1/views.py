from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.v1.serializers import CategoriaSerializer, PostSerializer
from core.models import Category, Post


class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer