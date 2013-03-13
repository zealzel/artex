# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'address.COU'
        db.delete_column(u'CRM_address', 'COU')

        # Deleting field 'address.CUS'
        db.delete_column(u'CRM_address', 'CUS')

        # Deleting field 'address.DIS'
        db.delete_column(u'CRM_address', 'DIS')

        # Adding field 'address.CO'
        db.add_column(u'CRM_address', 'CO',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'address.DI'
        db.add_column(u'CRM_address', 'DI',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'address.CU'
        db.add_column(u'CRM_address', 'CU',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'address.COU'
        db.add_column(u'CRM_address', 'COU',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'address.CUS'
        db.add_column(u'CRM_address', 'CUS',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'address.DIS'
        db.add_column(u'CRM_address', 'DIS',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Deleting field 'address.CO'
        db.delete_column(u'CRM_address', 'CO')

        # Deleting field 'address.DI'
        db.delete_column(u'CRM_address', 'DI')

        # Deleting field 'address.CU'
        db.delete_column(u'CRM_address', 'CU')


    models = {
        u'CRM.address': {
            'CO': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'CU': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'DI': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '1'}),
            'Meta': {'ordering': "['id']", 'object_name': 'address'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.country']"}),
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
            'Meta': {'ordering': "['id']", 'object_name': 'country'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'CRM.county': {
            'Meta': {'ordering': "['id']", 'object_name': 'county'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'CRM.customer': {
            'Meta': {'ordering': "['id']", 'object_name': 'customer'},
            'birthday_day': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'birthday_month': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'birthday_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'suggestion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'CRM.district': {
            'Meta': {'ordering': "('id',)", 'object_name': 'district'},
            'county_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.county']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'CRM.email': {
            'Meta': {'ordering': "['id']", 'object_name': 'email'},
            'cus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.customer']"}),
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