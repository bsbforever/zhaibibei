# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0010_oraerror'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oraerror',
            name='error_message',
            field=models.TextField(),
        ),
    ]
