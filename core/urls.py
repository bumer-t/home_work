# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, url
from core.views import task_3, main_view


urlpatterns = patterns('',
   (r'^$',              main_view),
    url(r'^task-3$',    task_3,     name='task_3'),
)
