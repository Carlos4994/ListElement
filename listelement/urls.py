from django.contrib import admin
from django.urls import path

from rest_framework import routers

from .viewssets import ElementViewsSet

route = routers.SimpleRouter()
route.register('element',ElementViewsSet)

urlpatterns = route.urls
