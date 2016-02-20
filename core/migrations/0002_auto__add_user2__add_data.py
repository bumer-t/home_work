# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User2'
        db.create_table(u'core_user2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('core', ['User2'])

        # Adding model 'Data'
        db.create_table(u'core_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Data'])

        # Adding M2M table for field user on 'Data'
        m2m_table_name = db.shorten_name(u'core_data_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('data', models.ForeignKey(orm[u'core.data'], null=False)),
            ('user2', models.ForeignKey(orm['core.user2'], null=False))
        ))
        db.create_unique(m2m_table_name, ['data_id', 'user2_id'])


    def backwards(self, orm):
        # Deleting model 'User2'
        db.delete_table(u'core_user2')

        # Deleting model 'Data'
        db.delete_table(u'core_data')

        # Removing M2M table for field user on 'Data'
        db.delete_table(db.shorten_name(u'core_data_user'))


    models = {
        u'core.data': {
            'Meta': {'object_name': 'Data'},
            'data': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'core_data_Users2'", 'symmetrical': 'False', 'to': "orm['core.User2']"})
        },
        'core.user': {
            'Meta': {'ordering': "['id']", 'object_name': 'User'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.user2': {
            'Meta': {'ordering': "['id']", 'object_name': 'User2'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['core']