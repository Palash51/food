# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import OrderMeal 
# # Register your models here.
admin.site.register(OrderMeal)

class OrderMealAdmin(admin.ModelAdmin):

	list_display = (
        'name', 'mobile', 'thali', 'message')