# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 17:05
from __future__ import unicode_literals

import apps.companies.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0003_auto_20170210_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=45)),
                ('current_status', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=100)),
                ('service_description', models.TextField(max_length=10000)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
            ],
        ),
    ]