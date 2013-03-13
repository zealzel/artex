# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'address.county'
        db.delete_column(u'CRM_address', 'county')

        # Deleting field 'address.cus'
        db.delete_column(u'CRM_address', 'cus')

        # Deleting field 'address.district'
        db.delete_column(u'CRM_address', 'district')


        # Renaming column for 'address.country' to match new field type.
        db.rename_column(u'CRM_address', 'country', 'country_id')
        # Changing field 'address.country'
        db.alter_column(u'CRM_address', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.phone']))
        # Adding index on 'address', fields ['country']
        db.create_index(u'CRM_address', ['country_id'])


    def backwards(self, orm):
        # Removing index on 'address', fields ['country']
        db.delete_index(u'CRM_address', ['country_id'])

        # Adding field 'address.county'
        db.add_column(u'CRM_address', 'county',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'address.cus'
        db.add_column(u'CRM_address', 'cus',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'address.district'
        db.add_column(u'CRM_address', 'district',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)


        # Renaming column for 'address.country' to match new field type.
        db.rename_column(u'CRM_address', 'country_id', 'country')
        # Changing field 'address.country'
        db.alter_column(u'CRM_address', 'country', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        u'CRM.address': {
            'Meta': {'ordering': "['id']", 'object_name': 'address'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CRM.phone']"}),
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