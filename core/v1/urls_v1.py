from django.urls import path
from core.v1.views import ListView,ListDetailView,ItemView,ItemDetailView
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
    path('list', ListView.as_view()),
    path('list/<int:pk>', ListDetailView.as_view()),
    path('item', ItemView.as_view()),
    path('item/<int:pk>', ItemDetailView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),   
]