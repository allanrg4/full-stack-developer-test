from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from assignments.models import Assignment
from assignments.serializers import AssigmentSerializer


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssigmentSerializer
    permission_classes = [IsAuthenticated]
