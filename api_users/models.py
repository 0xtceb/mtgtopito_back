# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Deck(models.Model):
    user = models.ForeignKey(User, default=None, blank=True)
    commander = models.ForeignKey("Card", default=None, blank=True)
    name = models.CharField(max_length=200)

class Card(models.Model):
    multiverseid = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=1000)
    decks = models.ManyToManyField(Deck)
