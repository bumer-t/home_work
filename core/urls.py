# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from core.views import main_view, task_query
from core.tools.tasks import TASK_NUMBER_3, TASK_NUMBER_4


urlpatterns = patterns('',
   (r'^$',              main_view),
    url(r'^task-3$',    task_query, {'task_id': TASK_NUMBER_3},   name='task_query_3'),
    url(r'^task-4$',    task_query, {'task_id': TASK_NUMBER_4},   name='task_query_4'),
)
