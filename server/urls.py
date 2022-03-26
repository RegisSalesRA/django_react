from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.v1.views import ScheduleView
from core.views_tokens import BlacklistTokens

router = routers.DefaultRouter()
router.register(r'schedule', ScheduleView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.v1.urls_v1')),
    path('api/schedule/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', BlacklistTokens.as_view(),
         name='blacklist')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)