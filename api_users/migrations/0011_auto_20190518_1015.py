# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-18 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0010_deckcards'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeckCards',
            new_name='DeckCard',
        ),
    ]
