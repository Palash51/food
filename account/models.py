# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models import (
    Model,
    ForeignKey,
    OneToOneField,
    ManyToManyField,
    CharField,
    TextField,
    BooleanField,
    DateField,
    DateTimeField,
    IntegerField,
)

# Create your models here.
# class Registration(models.Model):
# 	Name = models.CharField(max_length=30, blank=False)
# 	Email = models.CharField(max_length=255, blank=False)
# 	Password = models.CharField(max_length=30, blank=False)
# 	Password2 = models.CharField(max_length=30, blank=False)

class OrderMeal(models.Model):
	name = models.CharField(max_length=30, blank=True)
	mobile = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=30, blank=True)
	thali = models.IntegerField(default=0,blank=True)
	delivery_date = DateTimeField(blank=True, null=True)
	message = models.CharField(max_length=100, blank=True)

	