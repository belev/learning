from django.conf.urls import patterns, url
from post import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )
