# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    user = models.ForeignKey(User, default=None, blank=True)
    commander = models.ForeignKey("Card", default=None, blank=True, related_name='commander', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ligues = models.ManyToManyField("Ligue", default=None, blank=True)

    def __str__(self):
        return '%s' % self.name

class Card(models.Model):
    multiverseid = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=1000)
    quantity = models.IntegerField(default=1)
    type = models.CharField(max_length=100, default=None, null=True, blank=True)
    deck = models.ForeignKey(Deck, default=None, related_name='cards', null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

class Ligue(models.Model):
    name = models.CharField(max_length=200)
    decks = models.ManyToManyField(Deck)

    def __str__(self):
        return '%s : %s joueur(s)' % (self.name, self.decks.count())

class Score(models.Model):
    ligue =  models.ForeignKey(Ligue)
    deck_one = models.ForeignKey(Deck, related_name='deck_one', default=None)
    deck_two = models.ForeignKey(Deck, related_name='deck_two', default=None)
    results = models.IntegerField(default=0)

    def __str__(self):
        return '%s VS %s | score %s' % (self.deck_one.name,
                                        self.deck_two.name,
                                        self.results)
