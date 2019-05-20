"""api_mtgtopito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api_users.views import UserViewSet, DeckViewSet, CardViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'decks', DeckViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    url(r'^api/login/', obtain_auth_token),
    url(r'^api/', include(router.urls)),
    url(r'^api/admin/', admin.site.urls),
]
