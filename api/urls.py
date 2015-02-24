from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
        url(r'^charts/$', views.ChartsList().as_view()),
        url(r'^charts/(?P<pk>[0-9]+)/$', views.EachCharts().as_view()),
        url(r'^users/$', views.UserList().as_view()),
        url(r'^users/(?P<id>[0-9]+)/$', views.UserDetail().as_view()),
        url(r'^api-access/', include('rest_framework.urls'
                                    , namespace='rest_framework'))
        ]
