from rest_framework import viewsets

from .models import Workday, Schedule
from .serializer import WorkdaySerializer, ScheduleSerializer


class WorkdayViewSet(viewsets.ModelViewSet):
    queryset = Workday.objects.all()
    serializer_class = WorkdaySerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
