# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workday, Schedule

# Django Rest Framework
from rest_framework import viewsets
from .serializers import WorkdaySerializer, ScheduleSerializer


# Views from Workdays.
class WorkdayList(ListView):
    model = Workday


class WorkdayDetailView(DetailView):
    model = Workday
    template_name = 'workdays/workday_detail.html'


class WorkdayCreate(CreateView):
    model = Workday
    success_url = reverse_lazy('workday_list')
    fields = ['code', 'name', 'schedule']
    template_name = 'workdays/workday_create.html'


class WorkdayUpdate(UpdateView):
    model = Workday
    success_url = reverse_lazy('workday_list')
    fields = ['name', 'schedule']
    template_name = 'workdays/workday_update.html'


class WorkdayDelete(DeleteView):
    model = Workday
    success_url = reverse_lazy('workday_list')
    template_name = 'workdays/workday_delete.html'


# Views from Schedules
class ScheduleListView(ListView):
    model = Schedule
    paginate_by = 10
    template_name = 'schedules/schedule_list.html'


class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedules/schedule_detail.html'


class ScheduleCreateView(CreateView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')
    fields = ['day', 'time_start', 'time_end']
    template_name = 'schedules/schedule_create.html'


class ScheduleUpdateView(UpdateView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')
    fields = ['day', 'time_start', 'time_end']
    template_name = 'schedules/schedule_update.html'


class ScheduleDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')
    template_name = 'schedules/schedule_delete.html'


# API views
class WorkdayViewSet(viewsets.ModelViewSet):
    queryset = Workday.objects.all().order_by('code')
    serializer_class = WorkdaySerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('pk')
    serializer_class = ScheduleSerializer
