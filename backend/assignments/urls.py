from rest_framework.routers import DefaultRouter

from assignments.views import AssignmentViewSet


router = DefaultRouter()

router.register('assignments', AssignmentViewSet, basename='assignments')

urlpatterns = router.urls
