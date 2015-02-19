from django.conf.urls import patterns, url

from . import views

urlpatterns = [
        url(r'^charts/$', views.chartList),
        url(r'^index/$', views.index)
        ]
