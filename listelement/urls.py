from django.contrib import admin
from django.urls import path

from rest_framework import routers

from .viewssets import ElementViewsSet, CategoryViewsSet, TypeViewsSet

route = routers.SimpleRouter()
route.register('element',ElementViewsSet)
route.register('category',CategoryViewsSet)
route.register('type',TypeViewsSet)

urlpatterns = route.urls
