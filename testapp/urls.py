# myproject/urls.py

from django.urls import path
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()

from .views import *

router.register(r'testapi',testview)

urlpatterns = [
    path('test/', views.test, name='test'),
    path('hello/', views.hello, name='hello'),
    path('add/', views.add_numbers, name='add-numbers'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    
]
