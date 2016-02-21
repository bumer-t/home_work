# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from shop.views import create



urlpatterns = patterns('',
   url(r'^create$', create),
)
