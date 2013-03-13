# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'customer.birthday_year'
        db.add_column('CRM_customer', 'birthday_year',
                      self.gf('django.db.models.fields.CharField')(default='1970', max_length=4, blank=True),
                      keep_default=False)

        # Adding field 'customer.birthday_month'
        db.add_column('CRM_customer', 'birthday_month',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'customer.birthday_day'
        db.add_column('CRM_customer', 'birthday_day',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'customer.birthday_year'
        db.delete_column('CRM_customer', 'birthday_year')

        # Deleting field 'customer.birthday_month'
        db.delete_column('CRM_customer', 'birthday_month')

        # Deleting field 'customer.birthday_day'
        db.delete_column('CRM_customer', 'birthday_day')


    models = {
        'CRM.address': {
            'Meta': {'object_name': 'address'},
            'country_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.country']"}),
            'county_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.county']"}),
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'district_id': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['CRM.district']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'CRM.country': {
            'Meta': {'object_name': 'country'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'CRM.county': {
            'Meta': {'object_name': 'county'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'CRM.customer': {
            'Meta': {'object_name': 'customer'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'birthday_day': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '2', 'blank': 'True'}),
            'birthday_month': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '2', 'blank': 'True'}),
            'birthday_year': ('django.db.models.fields.CharField', [], {'default': "'1970'", 'max_length': '4', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'suggestion': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        },
        'CRM.district': {
            'Meta': {'object_name': 'district'},
            'county_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.county']"}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'CRM.email': {
            'Meta': {'object_name': 'email'},
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'CRM.phone': {
            'Meta': {'object_name': 'phone'},
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['CRM']