# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-29 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_auto_20180620_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cur_residence',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='skyid',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]