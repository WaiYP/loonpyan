# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-19 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='rsrv_char_field_1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='rsrv_char_field_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='rsrv_char_field_3',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]