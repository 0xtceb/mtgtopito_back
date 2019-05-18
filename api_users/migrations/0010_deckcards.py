# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-18 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0009_auto_20190516_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeckCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('card', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api_users.Card')),
                ('deck', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api_users.Deck')),
            ],
        ),
    ]
