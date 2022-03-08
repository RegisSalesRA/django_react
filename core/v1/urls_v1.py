from django.urls import path
from core.v1.views import PostListView, PostDetailView, CategoryDetailView,CategoryListView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Django React API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('post/',PostListView.as_view()),
    path('post/<int:pk>',PostDetailView.as_view()),
    path('category/',CategoryListView.as_view()),
    path('category/<int:pk>',CategoryDetailView.as_view()),    

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]