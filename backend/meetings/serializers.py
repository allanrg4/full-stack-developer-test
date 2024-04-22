from rest_framework import serializers

from meetings.models import Session


class SessionSerializer(serializers.ModelSerializer):
    assignments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Session
        fields = '__all__'

    @staticmethod
    def get_assignments(obj: Session):
        return obj.assignment_set.count()
