# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from shop.views import create_order, products_list, view_order


urlpatterns = patterns('',
   url(r'^products-list$',                      products_list,    name='products_list'),
   url(r'^create-order$',                       create_order,     name='create_order'),
   url(r'^view-order/(?P<order_id>\S+)$',       view_order,       name='view_order'),
)
