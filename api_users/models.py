# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    user = models.ForeignKey(User, default=None, blank=True)
    commander = models.ForeignKey("Card", default=None, blank=True, related_name='commander')
    name = models.CharField(max_length=200)
    ligues = models.ManyToManyField("Ligue", default=None, blank=True)

    def __str__(self):
        return '%s' % self.name

class Card(models.Model):
    multiverseid = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=1000)


    def __str__(self):
        return '%s' % self.name

class DeckCard(models.Model):
    deck = models.ForeignKey(Deck, default=None, blank=True)
    card = models.ForeignKey(Card, default=None, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s contient %s %s' % (  self.deck.name,
                                        self.quantity,
                                        self.card.name)

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
