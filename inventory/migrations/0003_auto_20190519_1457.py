# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-19 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190519_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='rsrv_char_field_1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='rsrv_char_field_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='rsrv_char_field_3',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
