# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0014_auto_20190523_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_users.Deck'),
        ),
    ]
