# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0007_auto_20190516_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='deck',
        ),
        migrations.AddField(
            model_name='score',
            name='deck_one',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_one', to='api_users.Deck'),
        ),
        migrations.AddField(
            model_name='score',
            name='deck_two',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_two', to='api_users.Deck'),
        ),
    ]
