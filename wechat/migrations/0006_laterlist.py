# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0005_auto_20161225_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='laterlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_link', models.CharField(max_length=100)),
                ('movie_pic', models.CharField(max_length=100)),
                ('movie_time', models.CharField(max_length=20)),
                ('movie_type', models.CharField(max_length=50)),
                ('movie_region', models.CharField(max_length=20)),
                ('movie_people', models.CharField(max_length=20)),
                ('movie_preview', models.CharField(max_length=100)),
            ],
        ),
    ]
