# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api_users.models import Deck, Card, Ligue, Score

# Register your models here.

admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Ligue)
admin.site.register(Score)
