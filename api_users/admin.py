# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api_users.models import Deck, Card, DeckCard, Ligue, Score

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = DeckCard

class DeckAdmin(admin.ModelAdmin):

    #def card_number(self, instance):
    #    return DeckCard.objects.filter(deck=instance).count()

    list_display = ['commander', 'name', 'card_number']
    list_filter = ('commander','name')
    inlines = [ChoiceInline]


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card)
admin.site.register(DeckCard)
admin.site.register(Ligue)
admin.site.register(Score)
