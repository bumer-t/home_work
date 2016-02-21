# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from shop.views import create_order, products_list


urlpatterns = patterns('',
   url(r'^products-list$',    products_list,    name='products_list'),
   url(r'^create-order$',     create_order,     name='create_order'),
)
