# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20180828_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
