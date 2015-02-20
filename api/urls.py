from django.conf.urls import patterns, url

from . import views

urlpatterns = [
        url(r'^charts/$', views.ChartsList().as_view()),
        url(r'^charts/(?P<id>[0-9]+)/$', views.EachChart().as_view())
        ]
