# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductType'
        db.create_table(u'shop_producttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 2, 21, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('amount_tax', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('shop', ['ProductType'])


    def backwards(self, orm):
        # Deleting model 'ProductType'
        db.delete_table(u'shop_producttype')


    models = {
        'shop.producttype': {
            'Meta': {'ordering': "['-created']", 'object_name': 'ProductType'},
            'amount_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 2, 21, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['shop']