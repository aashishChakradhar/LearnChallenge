from django.contrib import admin
from django.urls import path
from learnDjango import views
urlpatterns = [
    path('', views.Normal.as_view(), name='index'),
    path('index', views.Normal.as_view(), name='index'),
    path('auth', views.AuthView.as_view(), name='auth'),
]