
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
