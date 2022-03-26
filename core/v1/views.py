
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.v1.serializers import CategoriaSerializer, PostSerializer, YouTubeScheduleSerializer
from core.models import Category, Post, YouTubeSchedule


class PostListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
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


class ScheduleView(viewsets.ModelViewSet):
    serializer_class = YouTubeScheduleSerializer
    queryset = YouTubeSchedule.objects.all()