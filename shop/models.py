# -*- coding: utf-8 -*-
import re
from django.db import models
from django.utils.encoding import smart_str
from django.core.exceptions import ValidationError
from core.models import DateCreatedChanged
from core.tools.orders import products_count_amount, products_count_tax
from shop.consts.product import SOURCE


class TaxAbstract(models.Model):
    class Meta:
        abstract = True

    def get_tax(self, amount):
        if self.amount_tax == 0:
            return 0
        return round(amount * self.amount_tax / 100, 2)


class ProductType(DateCreatedChanged, TaxAbstract):
    name        = models.CharField('Наименование категории', max_length=40, unique=True, help_text=u'англ.раскладка')
    amount_tax  = models.DecimalField('Сумма налога', max_digits=4, decimal_places=2, help_text=u'пдв')

    class Meta:
        ordering            = ['-created']
        app_label           = 'shop'
        verbose_name_plural = u'Типы продуктов'

    def __unicode__(self):
        return u'%s' % (self.name,)

    def clean(self):
        super(ProductType, self).clean()
        if re.search('[а-яА-Я]', smart_str(self.name), re.UNICODE):
            raise ValidationError(u'только англ.раскладка')
        self.name = self.name.lower()


class SourceProduct(DateCreatedChanged, TaxAbstract):
    source      = models.BooleanField(u'Тип', choices=SOURCE.choices(), unique=True)
    amount_tax  = models.DecimalField('Сумма налога', max_digits=4, decimal_places=2, help_text=u'Налог на импорт')

    class Meta:
        ordering            = ['-created']
        app_label           = 'shop'
        verbose_name_plural = u'Источники продуктов'

    def __unicode__(self):
        return u'%s' % (SOURCE.dict()[self.source],)


class Product(DateCreatedChanged):
    id              = models.IntegerField(u'Код товара', primary_key=True, db_index=True, help_text=u'Штрих-код')
    name            = models.CharField('Наименование товара', max_length=100, help_text=u'англ.раскладка')
    product_type    = models.ForeignKey(ProductType, verbose_name=u'Тип продукта')
    source          = models.ForeignKey(SourceProduct, verbose_name=u'Источник')
    amount          = models.DecimalField('Себестоимость товара', max_digits=10, decimal_places=2, help_text=u'без учёта налога')

    class Meta:
        ordering            = ['-created']
        app_label           = 'shop'
        verbose_name_plural = u'Продукты'

    def __unicode__(self):
        return u'%s_%s' % (self.id, self.name)

    @property
    def total_tax(self):
        return self.product_type.get_tax(self.amount) + self.source.get_tax(self.amount)

    @property
    def total_amount(self):
        return round(float(self.amount) + self.total_tax, 2)

    @property
    def output(self):
        return {
            'id'            : self.id,
            'name'          : self.name,
            'product_type'  : {
                'name': self.product_type.name,
            },
            'amount'        : self.total_amount,
        }


class Order(DateCreatedChanged):
    # client
    products    = models.ManyToManyField(Product, related_name="%(app_label)s_%(class)s_products")
    amount      = models.DecimalField('∑', max_digits=10, decimal_places=2)
    tax_amount  = models.DecimalField('∑ Налога', max_digits=10, decimal_places=2)

    class Meta:
        ordering            = ['-created']
        app_label           = 'shop'
        verbose_name_plural = u'Заказы'

    def products_str(self, separator=''):
        return separator.join(unicode(x) for x in self.products.all())

    def create_order(self, products):
        """
        :type products_id: list
        """
        order = Order()
        order.amount        = products_count_amount(products)
        order.tax_amount    = products_count_tax(products)
        order.save()
        order.products.add(*products)

    @property
    def output(self):
        return {
                'amount'        : float(self.amount),
                'tax_amount'    : float(self.tax_amount),
                'products'      : sorted([p.output for p in self.products.all()], key=lambda k: k['id'])
        }
