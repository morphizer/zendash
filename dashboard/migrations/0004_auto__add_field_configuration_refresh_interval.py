# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Configuration.refresh_interval'
        db.add_column('dashboard_configuration', 'refresh_interval',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Configuration.refresh_interval'
        db.delete_column('dashboard_configuration', 'refresh_interval')


    models = {
        'dashboard.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refresh_interval': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'show_acknowledged': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'zenoss_instance': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zenoss_password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zenoss_username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['dashboard']