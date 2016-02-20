# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home_work.views.home', name='home'),
    # url(r'^core/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^',           include('core.urls')),
)
