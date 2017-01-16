# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movielist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_link', models.CharField(max_length=100)),
                ('movie_actor', models.CharField(max_length=100)),
                ('movie_director', models.CharField(max_length=50)),
                ('movie_time', models.CharField(max_length=20)),
                ('movie_region', models.CharField(max_length=50)),
                ('movie_release', models.CharField(max_length=10)),
                ('movie_score', models.FloatField()),
                ('movie_pic', models.CharField(max_length=100)),
            ],
        ),
    ]
