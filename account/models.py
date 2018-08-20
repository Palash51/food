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
    SET_NULL,
    CASCADE,
    EmailField
)

from django.contrib.auth.models import User, Group

from mptt.models import MPTTModel, TreeForeignKey


class BusinessUnit(MPTTModel):
    """BusinessUnit example- sarvana hotel
    """
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=CASCADE,
    )
    name = CharField(
        max_length=100, unique=True, help_text="business unit name")

    def __str__(self):
        return self.name

    def employee_by_position(self, position_name):
        """returns employee filling a position"""
        return self.employment_set.filter(
            position__name=position_name,
        ).latest('employment_date').employee

    @property
    def restaurant_manager(self):
        """returns the restaurant manager of a business unit"""
        return self.employee_by_position('restaurant_manager')

    @property
    def restaurant_owner(self):
        """returns the restaurant owner of a business unit"""
        return BusinessUnit.objects.filter(
            level=0
        )[0].employee_by_position('restaurant_owner')


class Employee(Model):
    """employee model to add emp"""
    user = OneToOneField(
        User, related_name='employee', null=True, on_delete=SET_NULL)
    name = CharField(max_length=100, unique=True, help_text="employee name")
    email = EmailField(blank=False, null=False)

    @property
    def businessunit(self):
        """returns the business unit of an employee"""
        return self.employment_set.latest('employment_date').businessunit

    def __str__(self):
        return self.name


class Position(Model):
    """position model"""
    name = CharField(max_length=100)

    def __str__(self):
        return self.name

    def employee_for_businessunit(self, businessunit=None):
        """returns the employee filling the position in a business unit"""
        if not businessunit:
            businessunit = BusinessUnit.objects.get(level=0)
        return self.employment_set.filter(
            businessunit=businessunit,
        ).latest('-employment_date').employee


class Employment(MPTTModel):
    """employment model relates business unit to position to employee"""
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='reportees',
        on_delete=SET_NULL,
    )
    businessunit = ForeignKey(BusinessUnit, on_delete=CASCADE)
    position = ForeignKey(Position, on_delete=CASCADE)
    employee = ForeignKey(Employee, on_delete=CASCADE)
    employment_date = DateField(null=True)


class UserProfile(Model):

    """model holding relation between business unit and
    roles played by employee"""
    user = OneToOneField(User, on_delete=CASCADE,
                         null=True, related_name='profile')
    employee = ManyToManyField(
        Employee, related_name='profile')

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return u'Profile of user: {0}'.format(self.user.get_full_name())

    def has_perm(self, perm):
        """Returns if the employee has a particular permission"""
        perm = 'auth.' + perm.strip()
        return self.user.has_perm(perm)

    @property
    def username(self):
        """Returns the username of the profile user"""
        return self.user.username

    def user_groups(self):
        """returns the list of groups the user belongs to"""
        return self.user.groups.all().values_list('name', flat=True)

    @property
    def is_owner(self):
        """Checks if employee is owner of restaurant"""
        return 'restaurant_owner' in self.user_groups()

    @property
    def is_manager(self):
        """Checks if employee is manager of restaurant"""
        return 'restaurant_manager' in self.user_groups()

    def is_user(self, *groups):
        """Checks user is member of ALL groups"""
        return self.user.groups.filter(name__in=groups).exists()

    @property
    def businessunit(self):
        """Returns the businessunit of the employee"""
        return self.employee.businessunit


class OrderMeal(models.Model):
    name = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    thali = models.IntegerField(default=0, blank=True)
    delivery_date = DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=100, blank=True)
