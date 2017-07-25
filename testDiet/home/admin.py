# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Food, Data, Users

class FoodAdmin(admin.ModelAdmin):
    list_display = ('foodname','type','cost')
    search_fields = ('foodname','type','cost')
    list_filter = ('type',)

class DataAdmin(admin.ModelAdmin):
    list_display = ('name','type','picture')
    search_fields = ('name','type','picture')

# Register your models here.
admin.site.register(Food, FoodAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Users)
