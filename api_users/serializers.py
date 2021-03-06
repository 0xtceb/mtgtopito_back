# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import serializers
from api_users.models import Card, Deck, Ligue

if settings.ENABLE_TRANSACTIONNAL_MAILS:
    import base64
    from django.utils.http import urlsafe_base64_encode
    from django.utils.encoding import force_bytes
    from mailjet_rest import Client


class UserSerializer(serializers.HyperlinkedModelSerializer):
    recaptcha = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'password', 'recaptcha')

    def send_confirmation_email(self, user):
        confirmation_url = "http://TODOCONFIRMATIONURL/%s" % urlsafe_base64_encode(force_bytes(user.pk))
        api_key = settings.MAILJET_API_KEY
        api_secret = settings.MAILJET_SECRET_KEY
        data = {
          'Messages':   [{
                        "From": {
                            "Email": "%s" % settings.EMAIL_SENDER,
                            "Name": "MTG TOPITO"
                        },
                        "To": [
                            {
                                "Email": "%s" % user.email,
                                "Name": "%s" % user.username
                            }
                        ],
                        "Subject": "Email de confirmation MTG TOPITO",
                        "TextPart": "Votre inscription est bientôt terminée ! Voici votre lien de confirmation : %s" % confirmation_url,
                        "HTMLPart": "<h3>Votre inscription est bientôt terminée !</h3><a href='%s'>Voici votre lien de confirmation</a>" % confirmation_url
                        }]
        }

        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        mailjet.send.create(data=data)
        return

    def create(self, validated_data):
        recaptcha = None
        if not validated_data.get('recaptcha', None):
            raise serializers.ValidationError("Vous êtes un robot sir.")
        else:
            recaptcha = validated_data.pop("recaptcha")
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_SECRET,
            'response': recaptcha
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = json.load(response)
        if not result['success']:
            raise serializers.ValidationError('Vous êtes un robot sir.')
        user = User.objects.create_user(**validated_data)
        if settings.ENABLE_TRANSACTIONNAL_MAILS:
            self.send_confirmation_email(user)
        return user
        if User.objects.filter(email = validated_data['email']).count() == 0:
            user = User.objects.create_user(**validated_data)
            if settings.ENABLE_TRANSACTIONNAL_MAILS:
                self.send_confirmation_email(user)
            return user
        else:
            raise serializers.ValidationError('Cet email est déjà pris !')

class LigueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ligue
        fields = ('url', 'name', 'decks')

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('url', 'multiverseid', 'name', 'type', 'imageUrl', 'quantity', 'deck')

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    commander = CardSerializer(required=True)
    ligues = LigueSerializer(required=False, many=True)
    cards = CardSerializer(required=False, many=True)
    id = serializers.ReadOnlyField()
    class Meta:
        model = Deck
        fields = ('url', 'id', 'user', 'name', 'commander', 'ligues', 'cards')

    def create(self, validated_data):
        commander_data = validated_data.pop('commander')
        commander = Card.objects.create(**commander_data)
        cards_data = validated_data.pop('cards')
        deck = Deck.objects.create(commander=commander, **validated_data)
        for card in cards_data:
            Card.objects.create(deck=deck, **card)
        return deck

    def update(self, instance, validated_data):
        commander_data = validated_data.pop('commander')
        commander = instance.commander
        commander.multiverseid = commander_data.get('multiverseid', commander.multiverseid)
        commander.name = commander_data.get('name', commander.name)
        commander.type = commander_data.get('type', commander.type)
        commander.imageUrl = commander_data.get('imageUrl', commander.imageUrl)
        commander.quantity = 1
        commander.save()

        cards_data = validated_data.pop('cards')
        for card in cards_data:
            if not card.get('deck'):
                Card.objects.create(deck=instance, **card)


        instance.name = validated_data["name"]
        instance.save()
        return instance
