from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include([
        path('auth/token/', TokenObtainPairView.as_view()),
        path('auth/token/refresh/', TokenRefreshView.as_view()),
        path('auth/token/verify/', TokenVerifyView.as_view()),

        path('assignments/', include('assignments.urls')),

        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ])),
]
