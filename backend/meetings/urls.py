from rest_framework.routers import DefaultRouter

from meetings.views import SessionViewSet


router = DefaultRouter()

router.register('sessions', SessionViewSet, basename='sessions')

urlpatterns = router.urls
