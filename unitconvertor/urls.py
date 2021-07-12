from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'unitconvertor'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('convert/', views.convert, name='convert'),
    path('newconvert/', views.newconvert, name='newconvert')


]
