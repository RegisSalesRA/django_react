
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import BlacklistTokenUpdateView, PostListDetailfilter,CustomUserCreate

urlpatterns = [
    path('api/v1/', include('core.urls')),
    path('api/v1/search/', PostListDetailfilter.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/create/', CustomUserCreate.as_view(), name="create_user"),
    path('api/logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
