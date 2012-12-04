# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuration'
        db.create_table('dashboard_configuration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zenoss_instance', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('zenoss_username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('zenoss_password', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('dashboard', ['Configuration'])


    def backwards(self, orm):
        # Deleting model 'Configuration'
        db.delete_table('dashboard_configuration')


    models = {
        'dashboard.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zenoss_instance': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zenoss_password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zenoss_username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['dashboard']