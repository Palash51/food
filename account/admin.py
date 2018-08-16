# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import OrderMeal, UserProfile
# # Register your models here.
admin.site.register(OrderMeal)

class OrderMealAdmin(admin.ModelAdmin):

	list_display = (
        'name', 'mobile', 'thali', 'message')


class UserProfileAdmin(admin.ModelAdmin):
    """Admin class for UserProfile"""
    list_display = ['id', 'user', 'employee']
    list_filter = []
    fieldsets = [
        (None, {'fields': ['user', 'employee']}),
    ]


admin.site.register(UserProfile, UserProfileAdmin)