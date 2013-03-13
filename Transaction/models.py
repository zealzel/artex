# -*- coding:utf8 -*-
from django.db import models

class purchase(models.Model):
    class Meta:
        verbose_name=u'交易'
        verbose_name_plural=u'交易'
    #def __unicode__(self):
    #    return self.id
    order_date=models.DateField()
    cus_id=models.ForeignKey('CRM.customer')

class productType(models.Model):
    class Meta:
        verbose_name=u'產品種類'
        verbose_name_plural=u'產品種類'
    def __unicode__(self):
        return self.description
    description=models.CharField(max_length=30)

class product(models.Model):
    class Meta:
        verbose_name=u'產品'
        verbose_name_plural=u'產品'
    def __unicode__(self):
        return self.name
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=10)
    pType_id=models.ForeignKey('productType')
    
class purchaseItems(models.Model):
    class Meta:
        verbose_name=u'交易清單'
        verbose_name_plural=u'交易清單'
    #def __unicode__(self):
    #    return self.id
    purchase_id=models.ForeignKey('purchase')
    prod_id=models.ForeignKey('product')
    quantity=models.PositiveIntegerField()
    


