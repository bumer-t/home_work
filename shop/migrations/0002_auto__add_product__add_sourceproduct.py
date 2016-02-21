# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'shop_product', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 2, 21, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.ProductType'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.SourceProduct'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('shop', ['Product'])

        # Adding model 'SourceProduct'
        db.create_table(u'shop_sourceproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 2, 21, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.BooleanField')(unique=True)),
            ('amount_tax', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('shop', ['SourceProduct'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'shop_product')

        # Deleting model 'SourceProduct'
        db.delete_table(u'shop_sourceproduct')


    models = {
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