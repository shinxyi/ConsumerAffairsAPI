# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loginreg.User'),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
