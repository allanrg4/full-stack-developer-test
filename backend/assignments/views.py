from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from assignments.models import Assignment
from assignments.serializers import AssigmentSerializer


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssigmentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Validate POST data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the session has availability
        session = serializer.validated_data['session']
        if session.assignment_set.count() >= session.availability:
            return Response({
                'message': 'La sesión ya no tiene disponibilidad para asignar más estudiantes.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check if the student is already assigned to the session
        student = serializer.validated_data['student']
        if student.assignment_set.filter(session=session).exists():
            return Response({
                'message': 'El estudiante ya está asignado a la sesión.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check if the student is already assigned to another session at the same time
        crossed_assignments = student.assignment_set.filter(
            session__start_datetime__lte=session.end_datetime,
            session__end_datetime__gte=session.start_datetime
        ).exists()

        if crossed_assignments:
            return Response({
                'message': 'El estudiante ya está asignado a otra sesión en el mismo horario.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Create the assignment
        return super().create(request, *args, **kwargs)
