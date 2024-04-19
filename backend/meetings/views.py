from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from meetings.models import Session
from meetings.serializers import SessionSerializer


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]
