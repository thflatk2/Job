# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-19 11:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0009_auto_20180619_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_info',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2018, 6, 19, 11, 48, 30, 949595, tzinfo=utc)),
        ),
    ]
