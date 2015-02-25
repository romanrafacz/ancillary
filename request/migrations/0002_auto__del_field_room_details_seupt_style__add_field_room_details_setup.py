# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Room_Details.seupt_style'
        db.delete_column(u'request_room_details', 'seupt_style')

        # Adding field 'Room_Details.setup_style'
        db.add_column(u'request_room_details', 'setup_style',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Room_Details.seupt_style'
        db.add_column(u'request_room_details', 'seupt_style',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Deleting field 'Room_Details.setup_style'
        db.delete_column(u'request_room_details', 'setup_style')


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
            'setup_style': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['request']