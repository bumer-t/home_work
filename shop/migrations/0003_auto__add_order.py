# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'shop_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 2, 21, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('tax_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('shop', ['Order'])

        # Adding M2M table for field products on 'Order'
        m2m_table_name = db.shorten_name(u'shop_order_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['shop.order'], null=False)),
            ('product', models.ForeignKey(orm['shop.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['order_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'shop_order')

        # Removing M2M table for field products on 'Order'
        db.delete_table(db.shorten_name(u'shop_order_products'))


    models = {
        'shop.order': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Order'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 2, 21, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'shop_order_products'", 'symmetrical': 'False', 'to': "orm['shop.Product']"}),
            'tax_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'shop.product': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Product'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 2, 21, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.ProductType']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.SourceProduct']"})
        },
        'shop.producttype': {
            'Meta': {'ordering': "['-created']", 'object_name': 'ProductType'},
            'amount_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 2, 21, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'shop.sourceproduct': {
            'Meta': {'ordering': "['-created']", 'object_name': 'SourceProduct'},
            'amount_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 2, 21, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.BooleanField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['shop']