# -*- coding: utf-8 -*-
import json
import datetime as dt
from core.tools.orders import products_count_amount
from django import forms
from django.core.exceptions import ValidationError
from shop.consts.request_params import REQ_CREATE_ORDER
from shop.models import Product, Order


class OrderCreateForm(forms.Form):
    amount          = forms.DecimalField(max_digits=10, decimal_places=2, required=True, help_text=u'Общая стоимость заказа')
    products_id     = forms.CharField(required=True, help_text=u'["4820024700011","4820024700012","4820024700013"]')

    def clean(self):
        cleaned_data = super(OrderCreateForm, self).clean()
        if self.errors:
            return cleaned_data

        self.__check_amount(cleaned_data=cleaned_data)
        return cleaned_data

    def clean_products_id(self):
        products_id = json.loads(self.cleaned_data[REQ_CREATE_ORDER.PRODUCTS_ID])

        products = Product.objects.filter(id__in=products_id)
        if len(products_id) != len(products):
            raise ValidationError(u'Некорректный продукт')

        return products

    def __check_amount(self, cleaned_data):
        amount = cleaned_data[REQ_CREATE_ORDER.AMOUNT_SIG]
        products = cleaned_data[REQ_CREATE_ORDER.PRODUCTS_ID]
        if float(amount) != products_count_amount(products):
            raise ValidationError(u'переоценка')


class OrderViewForm(forms.Form):
    order_id = forms.IntegerField(min_value=0, max_value=99999999, required=True, help_text=u'id заказа')

    def clean_order_id(self):
        order_id = self.cleaned_data['order_id']
        try:
            return Order.objects.get(id=order_id) #client
        except Order.DoesNotExist:
            raise ValidationError(u'не верный ID')
