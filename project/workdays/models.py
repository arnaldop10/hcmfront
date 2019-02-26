# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Workday(models.Model):
    code = models.CharField('Codigo', max_length=2)
    name = models.CharField('Nombre', max_length=100)
    schedule = models.ManyToManyField('Schedule', related_name='workdays')

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'

    def __unicode__(self):
        return self.name


class Schedule(models.Model):
    DAYS = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('X', 'Miércoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo')
    )
    day = models.CharField(u'Día', max_length=1, choices=DAYS, default='L')
    time_start = models.TimeField('Hora Entrada', default='08:00')
    time_end = models.TimeField('Hora Salida', default='17:00')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['id']

    def __unicode__(self):
        return '%s de %s - %s' % (
            self.get_day_display(), self.time_start, self.time_end)
