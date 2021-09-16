from rest_framework import viewsets
from ..models.schedule import Schedule
from ..serializers.schedule_serializer import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
