from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'workday', views.WorkdayViewSet)
router.register(r'schedule', views.ScheduleViewSet)

urlpatterns = [
    # Workdays urls
    url(r'^$', views.WorkdayList.as_view(), name='workday_list'),
    url(r'^(?P<pk>[0-9]+)$', views.WorkdayDetailView.as_view(),
        name='workday_detail'),
    url(r'^create/$', views.WorkdayCreate.as_view(), name='workday_create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.WorkdayUpdate.as_view(),
        name='workday_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.WorkdayDelete.as_view(),
        name='workday_delete'),

    # Schedules urls
    url(r'^schedule/list/$', views.ScheduleListView.as_view(),
        name='schedule_list'),
    url(r'^schedule/detail/(?P<pk>[0-9]+)/$',
        views.ScheduleDetailView.as_view(),
        name='schedule_detail'),
    url(r'^schedule/create/$', views.ScheduleCreateView.as_view(),
        name='schedule_create'),
    url(r'^schedule/update/(?P<pk>[0-9]+)/$',
        views.ScheduleUpdateView.as_view(),
        name='schedule_update'),
    url(r'^schedule/delete/(?P<pk>[0-9]+)/$',
        views.ScheduleDeleteView.as_view(),
        name='schedule_delete'),

    # API urls
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
]
