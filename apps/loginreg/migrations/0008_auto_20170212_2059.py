# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0007_merge_20170212_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 2, 12, 20, 59, 39, 475351)),
        ),
    ]
