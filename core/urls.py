# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, url
from core.views import main_view, task_3, task_4


urlpatterns = patterns('',
   (r'^$',              main_view),
    url(r'^task-3$',    task_3,     name='task_3'),
    url(r'^task-4$',    task_4,     name='task_4'),
)
