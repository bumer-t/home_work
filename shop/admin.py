# -*- coding: utf-8 -*-
from django.contrib import admin
from shop.models import ProductType, Product, SourceProduct


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


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(SourceProduct, SourceProductAdmin)
admin.site.register(Product, ProductAdmin)
