# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'customer.birthday_year'
        db.delete_column(u'CRM_customer', 'birthday_year')

        # Deleting field 'customer.birthday_day'
        db.delete_column(u'CRM_customer', 'birthday_day')

        # Deleting field 'customer.birthday_month'
        db.delete_column(u'CRM_customer', 'birthday_month')


    def backwards(self, orm):
        # Adding field 'customer.birthday_year'
        db.add_column(u'CRM_customer', 'birthday_year',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4, blank=True),
                      keep_default=False)

        # Adding field 'customer.birthday_day'
        db.add_column(u'CRM_customer', 'birthday_day',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'customer.birthday_month'
        db.add_column(u'CRM_customer', 'birthday_month',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)


    models = {
        u'CRM.address': {
            'Meta': {'object_name': 'address'},
            'country_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.country']"}),
            'county_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.county']"}),
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'district_id': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['CRM.district']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'CRM.country': {
            'Meta': {'object_name': 'country'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'CRM.county': {
            'Meta': {'object_name': 'county'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'CRM.customer': {
            'Meta': {'object_name': 'customer'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'suggestion': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        },
        u'CRM.district': {
            'Meta': {'object_name': 'district'},
            'county_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.county']"}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'CRM.email': {
            'Meta': {'object_name': 'email'},
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'CRM.phone': {
            'Meta': {'object_name': 'phone'},
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['CRM']