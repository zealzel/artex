# -*- coding:utf8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from smart_selects.db_fields import ChainedForeignKey
from datetime import datetime

class phone(models.Model):
    HOME='H'
    OFFICE='O'
    MOBILE='M'
    PHONE_TYPE_CHOICES=((HOME,u'住家'),(OFFICE,u'公司 '),(MOBILE,u'手機'))
    
    class Meta:
        verbose_name=u'電話'
        verbose_name_plural=u'電話'
        ordering=['id',]
    
    def __unicode__(self):
        return self.number

    number=models.CharField(max_length=20,verbose_name=u'電話/手機號碼')
    phone_type=models.CharField(max_length=2,choices=PHONE_TYPE_CHOICES,verbose_name=u'種類')
    cus=models.ForeignKey('customer',verbose_name=u'顧客')
    is_for_contact=models.BooleanField(default=True,verbose_name=u'主要聯絡電話')
    date_from=models.DateField(blank=True,null=True,verbose_name=u'有效日期')
    date_to=models.DateField(blank=True,null=True,verbose_name=u'失效日期')

class email(models.Model):
    class Meta:
        verbose_name=u'電子郵件'
        verbose_name_plural=u'電子郵件'
        ordering=['id',]
    def __unicode__(self):
        return self.email_address
    email_address=models.CharField(max_length=50,verbose_name=u'Email地址')
    #cus_id=models.ForeignKey('customer',verbose_name=u'顧客')
    cus=models.ForeignKey('customer',verbose_name=u'顧客')
    is_for_contact=models.BooleanField(default=True,verbose_name=u'主要聯絡email')
    date_from=models.DateField(blank=True,null=True,verbose_name=u'有效日期')
    date_to=models.DateField(blank=True,null=True,verbose_name=u'失效日期')
    
class country(models.Model):
    class Meta:
        verbose_name=u'國家'
        verbose_name_plural=u'國家'
        ordering=['id',]
    
    def __unicode__(self):
        return self.name
    id=models.IntegerField(primary_key=True,verbose_name=u'編號')
    name=models.CharField(max_length=20,verbose_name=u'名稱')

class county(models.Model):
    class Meta:
        verbose_name=u'縣市'
        verbose_name_plural=u'縣市'
        ordering=['id',]
    def __unicode__(self):
        return self.name
    id=models.IntegerField(primary_key=True,verbose_name=u'編號')
    name=models.CharField(max_length=10,verbose_name=u'名稱')

class district(models.Model):
    class Meta:
        verbose_name=u'行政區'
        verbose_name_plural='行政區'
        ordering=('id',)
        
    def __unicode__(self):
        return self.name    
    id=models.IntegerField(primary_key=True,verbose_name=u'編號')
    name=models.CharField(max_length=10,verbose_name=u'名稱')
    zip=models.CharField(max_length=5,verbose_name=u'ZIP碼')
    county=models.ForeignKey(county)

class customer(models.Model):
    class Meta:
        ordering=['id',]
        verbose_name=u'顧客'
        verbose_name_plural=u'顧客'
    def __unicode__(self):
        return self.name
    M='m'
    F='f'
    GENDER_CHOICES=((M,u'男'),(F,u'女'))
    #
    thisyear=datetime.now().year
    BIRTHDAY_YEAR_CHOICES=tuple([(str(i),str(i)) for i in range(1930,thisyear)])
    BIRTHDAY_MONTH_CHOICES=tuple([(str(i+1),str(i+1)) for i in range(12)])
    BIRTHDAY_DAY_CHOICES=tuple([(str(i+1),str(i+1)) for i in range(31)])
    #import pdb;pdb.set_trace()    
    name=models.CharField(max_length=50,verbose_name=u'姓名')
    gender=models.CharField(max_length=2,choices=GENDER_CHOICES,verbose_name=u'性別')
    #birthday=models.DateField(verbose_name=u'生日',blank=True,null=True)
    #
    
    birthday_year=models.CharField(max_length=4,choices=BIRTHDAY_YEAR_CHOICES, \
                                   verbose_name=u'年份',blank=True)
    birthday_month=models.CharField(max_length=2,choices=BIRTHDAY_MONTH_CHOICES, \
                                    verbose_name=u'月',blank=True)
    birthday_day=models.CharField(max_length=2,choices=BIRTHDAY_DAY_CHOICES, \
                                  verbose_name=u'日',blank=True)
    #
    suggestion=models.TextField(max_length=100,verbose_name=u'建議',blank=True)
    notes=models.TextField(max_length=100,verbose_name=u'註記',blank=True)

class address(models.Model):
    class Meta:
        verbose_name=u'地址'
        verbose_name_plural=u'地址'
        ordering=['id',]
    def __unicode__(self):
        return u"%s %s %s"%(self.country,self.district,self.location)
    country=models.ForeignKey(country,verbose_name=u'國家')
    county=models.ForeignKey(county,verbose_name=u'縣市')
    district= ChainedForeignKey(
       district, 
       chained_field='county',
       chained_model_field='county', 
       show_all=False, 
       auto_choose=True,
       verbose_name=u'行政區'
       )    
    location=models.CharField(max_length=50,verbose_name=u'地址')
    cus=models.ForeignKey(customer,verbose_name=u'顧客')
    is_for_contact=models.BooleanField(default=True,verbose_name=u'主要聯絡地址')
    date_from=models.DateField(blank=True,null=True,verbose_name=u'有效日期')
    date_to=models.DateField(blank=True,null=True,verbose_name=u'失效日期')
    





