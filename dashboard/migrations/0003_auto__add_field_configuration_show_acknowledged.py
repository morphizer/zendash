# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Configuration.show_acknowledged'
        db.add_column('dashboard_configuration', 'show_acknowledged',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Configuration.show_acknowledged'
        db.delete_column('dashboard_configuration', 'show_acknowledged')


    models = {
        'dashboard.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_acknowledged': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'zenoss_instance': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zenoss_password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zenoss_username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['dashboard']