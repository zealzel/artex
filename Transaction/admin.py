# -*- coding:utf8 -*-
from datetime import date

from django.contrib.contenttypes import generic
from django import forms
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.widgets import FileInput
from django.forms.widgets import ClearableFileInput

from django.contrib.admin import SimpleListFilter
from django.contrib.admin import BooleanFieldListFilter
#
#from PIL import Image
#
from models import purchase,productType,product,purchaseItems

#import pdb;pdb.set_trace()

class purchaseItemsInline(admin.TabularInline):
    model=purchaseItems
    extra=1

class purchaseAdmin(admin.ModelAdmin):
    inlines=[purchaseItemsInline,]

class productAdmin(admin.ModelAdmin):
    pass

#
admin.site.register(product)
admin.site.register(productType)
admin.site.register(purchase,purchaseAdmin)
admin.site.register(purchaseItems)
