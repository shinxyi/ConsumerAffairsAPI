# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 20:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20170212_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 12, 20, 15, 31, 784819)),
        ),
    ]
