# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from shop.consts.request_params import REQ_CREATE_ORDER
from core.decorators.request_decorators import api_view_500
from core.tools.response_helper import response_error, response_success
from shop.forms import OrderCreateForm, OrderViewForm
from shop.models import Product, Order


@require_POST
@api_view_500()
@csrf_exempt
def create_order(request):
    
    form = OrderCreateForm(request.POST)
    if not form.is_valid():
        return response_error('%s' % form.errors,)

    Order().create_order(form.cleaned_data[REQ_CREATE_ORDER.PRODUCTS_ID])

    params = {'status': 'created'}
    return response_success(params=params)


@require_GET
@api_view_500()
@csrf_exempt
def products_list(request):
    params = {'products': [p.output for p in Product.objects.all()]}
    return response_success(params=params)


@require_GET
@api_view_500()
@csrf_exempt
def view_order(request, order_id):
    
    form = OrderViewForm({'order_id' : order_id})
    if not form.is_valid():
        return response_error('%s' % form.errors,)

    return response_success(params={'order': form.cleaned_data['order_id'].output})
