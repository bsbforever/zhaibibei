# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0003_movielist_movie_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='tvlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_name', models.CharField(max_length=50)),
                ('tv_link', models.CharField(max_length=100)),
                ('tv_score', models.FloatField()),
                ('tv_pic', models.CharField(max_length=100)),
            ],
        ),
    ]
