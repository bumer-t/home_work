# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import FilteredSelectMultiple
from shop.models import ProductType, Product, SourceProduct, Order


class ProductTypeAdmin(admin.ModelAdmin):
    list_per_page   = 100
    list_display    = ('id', 'created', 'changed', 'name', 'amount_tax')
    search_fields   = ['id', 'name', 'amount_tax']


class SourceProductAdmin(admin.ModelAdmin):
    list_display    = ('created', 'changed', 'source', 'amount_tax')
    search_fields   = ['id', 'amount_tax']
    list_filter     = ('amount_tax',)


class ProductAdmin(admin.ModelAdmin):
    list_per_page   = 20
    list_display    = ('id', 'created', 'changed', 'name', 'product_type', 'source', 'amount', 'total_amount')
    search_fields   = ['product_type', 'amount']
    list_filter     = ('product_type', 'source',)

    def total_amount(self, obj):
        return obj.total_amount


class OrderForm(forms.ModelForm):

    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("products", False, attrs={'rows': '10'})
    )

    class Meta:
        model   = Order
        fields  = ['products', 'amount', 'tax_amount']


class OrdersAdmin(admin.ModelAdmin):
    list_per_page   = 20
    form            = OrderForm
    list_display    = ('products_custom', 'created', 'changed', 'amount', 'tax_amount')
    # readonly_fields = ['amount', 'tax_amount']
    list_filter = ('products__product_type', 'products__source',)

    def products_custom(self, object):
        return object.products_str('<br>')

    products_custom.short_description   = u'Заказ'
    products_custom.allow_tags          = True


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(SourceProduct, SourceProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrdersAdmin)
