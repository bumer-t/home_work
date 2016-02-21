# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from shop.models import Product, Order


@require_GET
@csrf_exempt
def create(request):

    products_id = [4820024700011, 4820024700012]
    products = Product.objects.filter(id__in=products_id)

    order = Order().create_order(products)

    params = {'status': 'create'}
    return HttpResponse(json.dumps(params), 'application/json')
