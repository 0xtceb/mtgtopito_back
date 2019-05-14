# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import serializers
from api_users.models import Card, Deck
import urllib
import urllib2
import json
class UserSerializer(serializers.HyperlinkedModelSerializer):
    recaptcha = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'password', 'recaptcha')

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

        if User.objects.filter(email = validated_data['email']).count() == 0:
            user = User.objects.create_user(**validated_data)
            return user
        else:
            raise serializers.ValidationError('Cet email est déjà pris !')

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('url', 'name', 'imageUrl')

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = ('url', 'name', 'commander')
