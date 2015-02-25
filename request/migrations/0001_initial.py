# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room_Details'
        db.create_table(u'request_room_details', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('request_date', self.gf('django.db.models.fields.DateField')()),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('room_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('attendance', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('est_budget', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('seupt_style', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'request', ['Room_Details'])


    def backwards(self, orm):
        # Deleting model 'Room_Details'
        db.delete_table(u'request_room_details')


    models = {
        u'request.room_details': {
            'Meta': {'object_name': 'Room_Details'},
            'attendance': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'est_budget': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'meeting_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'request_date': ('django.db.models.fields.DateField', [], {}),
            'room_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seupt_style': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['request']