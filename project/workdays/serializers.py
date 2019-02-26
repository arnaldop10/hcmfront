from rest_framework import serializers
from .models import Workday, Schedule


class WorkdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Workday
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
