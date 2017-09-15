# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0013_auto_20170302_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='lyrics',
            fields=[
                ('lyric_url', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('lyric_name', models.CharField(max_length=100)),
                ('lyric_title', models.CharField(max_length=100)),
                ('lyric_pic', models.CharField(max_length=100)),
                ('lyric_content', models.TextField()),
            ],
        ),
    ]