# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-18 01:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('address', models.CharField(max_length=30)),
                ('medical', models.BooleanField()),
                ('family', models.IntegerField()),
                ('education', models.CharField(choices=[('BA', 'BA'), ('history', 'History'), ('change in capital', 'Change in Capital'), ('share with voting right', 'Share with Voting Right'), ('dividend', 'Dividend')], default='A', max_length=15)),
                ('degree', models.CharField(max_length=20)),
                ('qualification', models.CharField(choices=[('aaa', 'Business Scope'), ('history', 'History'), ('change in capital', 'Change in Capital'), ('share with voting right', 'Share with Voting Right'), ('dividend', 'Dividend')], default='A', max_length=15)),
                ('qual_time', models.CharField(max_length=10)),
                ('resume', models.FileField(upload_to='')),
                ('letter', models.FileField(upload_to='')),
                ('photo', models.FileField(upload_to='')),
                ('office', models.CharField(choices=[('aaa', 'Business Scope'), ('history', 'History'), ('change in capital', 'Change in Capital'), ('share with voting right', 'Share with Voting Right'), ('dividend', 'Dividend')], default='A', max_length=15)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('wanted_salary', models.IntegerField()),
                ('prefer_location', models.CharField(max_length=15)),
                ('second_location', models.CharField(max_length=15)),
                ('prefer_class', models.CharField(choices=[('aaa', 'Business Scope'), ('history', 'History'), ('change in capital', 'Change in Capital'), ('share with voting right', 'Share with Voting Right'), ('dividend', 'Dividend')], default='A', max_length=15)),
                ('freind', models.BooleanField()),
                ('freind_name', models.CharField(max_length=15)),
                ('influx', models.CharField(choices=[('aaa', 'Business Scope'), ('history', 'History'), ('change in capital', 'Change in Capital'), ('share with voting right', 'Share with Voting Right'), ('dividend', 'Dividend')], default='A', max_length=10)),
                ('contact', models.CharField(max_length=20)),
                ('good_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('certification', models.BooleanField()),
                ('certification_text', models.CharField(max_length=20)),
                ('criminal', models.BooleanField()),
                ('criminal_text', models.CharField(max_length=20)),
                ('pet', models.BooleanField()),
                ('visa', models.CharField(max_length=10)),
                ('housing', models.BooleanField()),
                ('korean_level', models.CharField(choices=[('aaa', 'Business Scope'), ('history', 'History'), ('change in capital', 'Change in Capital'), ('share with voting right', 'Share with Voting Right'), ('dividend', 'Dividend')], default='A', max_length=15)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
