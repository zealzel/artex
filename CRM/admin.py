# -*- coding:utf8 -*-
from datetime import date
from datetime import datetime

from django.contrib.contenttypes import generic
from django import forms
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.widgets import FileInput
from django.forms.widgets import ClearableFileInput

from django.contrib.admin import SimpleListFilter
from django.contrib.admin import BooleanFieldListFilter
#
from django.core.mail import send_mail
#
#from PIL import Image
#
class MonthFilter(SimpleListFilter):
    title = _(u'每月生日')
    parameter_name = 'born_on_month'

    def lookups(self, request, model_admin):
        month=('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
        return [(i+1,month[i]) for i in range(12)]
    
    def queryset(self, request, queryset):
        for i in range(13):
            if self.value()==str(i):
                return queryset.filter(birthday_month=i)

class AgeGroupFilter(SimpleListFilter):
    title = _(u'年齡區間')
    parameter_name = 'age_group'

    def lookups(self, request, model_admin):
        group=('group1','group2','group3','group4','group5','group6','group7','group8','group9')
        ages=('0~9','10~19','20~29','30~39','40~49','50~59','60~69','70~79','80~89')
        return zip(group,ages)
    
    def queryset(self, request, queryset):
        for i in range(9):
            if self.value()=="group%s" % (i+1,):
                thisyear=datetime.now().year
                range_upper=thisyear-10*i
                range_lower=thisyear-10*(i+1)
                return queryset.filter(birthday_year__gt=range_lower,birthday_year__lte=range_upper)
     
from models import customer,address,country,county,district,phone,email

class phoneInline(admin.TabularInline):
    model=phone
    extra=1

class phoneAdmin(admin.ModelAdmin):
    search_fields=['number','cus__name']
    list_filter=('phone_type',)
    
class emailInline(admin.TabularInline):
    model=email
    extra=1

class emailAdmin(admin.ModelAdmin):    
    search_fields=['email_address','cus__name']
    
class addressInline(admin.TabularInline):
    model=address
    extra=1

class addressAdmin(admin.ModelAdmin):
    list_display=('id','country','county','district','location')
    search_fields=['id','county__name','district__name','location']
    list_filter=('county','district')
    
class customerAdmin(admin.ModelAdmin):
    '''
    actions = ['send_invite']
    def send_invite(self, request, queryset):
        # the below can be modified according to your application.
        # queryset will hold the instances of your model
        for profile in queryset:
            send_email(subject="Invite", message="Hello", from_eamil='myemail@mydomain.com', \
                       recipient_list=[profile.email]) # use your email function here
          
    send_invite.short_description = "Send invitation"
    '''  
    #change_list_template='admin/CRM/customer/change_list.html'
    '''
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        return super(customerAdmin, self).changelist_view(request,extra_context=extra_context)
    '''
    
    def show_birthday(self,obj):
        #import pdb;pdb.set_trace()
        year=u'年' if obj.birthday_year!='' else ''
        month=u'月' if obj.birthday_month!='' else ''
        day=u'日' if obj.birthday_day!='' else ''
        return u"%s%s%s%s%s%s" % (obj.birthday_year,year,obj.birthday_month,month,obj.birthday_day,day)
    show_birthday.short_description = u'生日'

    inlines=[phoneInline,emailInline,addressInline]
    search_fields=['id','name','suggestion','notes']

    fields=['name','gender',('birthday_year','birthday_month','birthday_day'),'suggestion','notes']
    list_filter=('gender',MonthFilter,AgeGroupFilter)
    list_display=('id','name','gender','show_birthday','suggestion','notes')
    list_display_links=('id','name')
 
    
class districtAdmin(admin.ModelAdmin):
    list_filter=('county',)
    list_display=('id','name')

admin.site.register(customer,customerAdmin)
admin.site.register(address,addressAdmin)
admin.site.register(email,emailAdmin)
admin.site.register(phone,phoneAdmin)

admin.site.register(country)
admin.site.register(county)
admin.site.register(district,districtAdmin)

