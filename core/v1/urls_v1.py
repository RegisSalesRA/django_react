from django.urls import path
from core.v1.views import PostListView, PostDetailView, CategoryDetailView,CategoryListView

urlpatterns = [
    path('post/',PostListView.as_view()),
    path('post/<int:pk>',PostDetailView.as_view()),
    path('category/',CategoryListView.as_view()),
    path('category/<int:pk>',CategoryDetailView.as_view()),    
]