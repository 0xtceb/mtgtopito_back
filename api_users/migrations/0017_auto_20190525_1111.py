# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0016_auto_20190525_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
