# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 20:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20170210_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 12, 20, 33, 19, 309318)),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
