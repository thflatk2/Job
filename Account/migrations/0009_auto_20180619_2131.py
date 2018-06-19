# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-19 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, choices=[('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('South Africa', 'South Africa'), ('New Zealand', 'New Zealand'), ('Australia', 'Australia')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cur_residence',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='degree',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('MAN', 'MAN'), ('WOMAN', 'WOMAN')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='letter',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='prefer_class',
            field=models.CharField(choices=[('Kindergarten', 'Kindergarten'), ('Elementary', 'Elementary'), ('Middle', 'Middle')], default='A', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='skyid',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='user_pic1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='user_pic2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
