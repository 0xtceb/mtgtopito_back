# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from django.contrib.auth.models import User
from serializers import UserSerializer, CardSerializer, DeckSerializer, LigueSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework import permissions
from api_users.models import Deck, Card, DeckCard, Ligue


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [(permissions.IsAuthenticatedOrReadOnly)]
    permission_classes = [(permissions.AllowAny)]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """def list(self, request):
        return Response(status=status.HTTP_200_OK)"""

    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated])
    def current(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(request.user, context=serializer_context)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request, pk=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class DeckViewSet(viewsets.ModelViewSet):
    permission_classes = [(permissions.AllowAny)]
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CardViewSet(viewsets.ModelViewSet):
    permission_classes = [(permissions.AllowAny)]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class LigueViewSet(viewsets.ModelViewSet):
    permission_classes = [(permissions.AllowAny)]
    queryset = Ligue.objects.all()
    serializer_class = LigueSerializer
