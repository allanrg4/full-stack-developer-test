from datetime import datetime

from django.db.models import Q
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from meetings.models import Session
from meetings.serializers import SessionSerializer


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action != 'list':
            return self.queryset

        date = self.request.query_params.get('date', None)
        if date is None:
            return self.queryset

        date = datetime.strptime(date, '%Y-%m-%d')
        date = timezone.make_aware(date)

        return self.queryset.filter(
            Q(start_datetime__date__lte=date) & Q(end_datetime__date__gte=date)
        )
