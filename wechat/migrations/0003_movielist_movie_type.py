# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_movielist'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='movie_type',
            field=models.CharField(default='nowplaying', max_length=20),
            preserve_default=False,
        ),
    ]
