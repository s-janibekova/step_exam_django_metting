from django.contrib import admin
from django.urls import path
from . import views

app_name = 'meetings'


urlpatterns = [
    path('', views.room_list, name='room_list'),
]
