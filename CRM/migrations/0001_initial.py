# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'phone'
        db.create_table('CRM_phone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cus_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.customer'])),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('CRM', ['phone'])

        # Adding model 'email'
        db.create_table('CRM_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cus_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.customer'])),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('CRM', ['email'])

        # Adding model 'country'
        db.create_table('CRM_country', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('CRM', ['country'])

        # Adding model 'county'
        db.create_table('CRM_county', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('CRM', ['county'])

        # Adding model 'district'
        db.create_table('CRM_district', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('county_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.county'])),
        ))
        db.send_create_signal('CRM', ['district'])

        # Adding model 'customer'
        db.create_table('CRM_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('suggestion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('CRM', ['customer'])

        # Adding model 'address'
        db.create_table('CRM_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.country'])),
            ('county_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.county'])),
            ('district_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['CRM.district'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cus_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CRM.customer'])),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('CRM', ['address'])


    def backwards(self, orm):
        # Deleting model 'phone'
        db.delete_table('CRM_phone')

        # Deleting model 'email'
        db.delete_table('CRM_email')

        # Deleting model 'country'
        db.delete_table('CRM_country')

        # Deleting model 'county'
        db.delete_table('CRM_county')

        # Deleting model 'district'
        db.delete_table('CRM_district')

        # Deleting model 'customer'
        db.delete_table('CRM_customer')

        # Deleting model 'address'
        db.delete_table('CRM_address')


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
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'suggestion': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'CRM.phone': {
            'Meta': {'object_name': 'phone'},
            'cus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['CRM.customer']"}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['CRM']