from django.contrib import admin
from django.urls import path
from learnDjango import views
urlpatterns = [
    #path("{urlpath}",{view class}, name="{reverse indexing}")
    path('', views.Normal.as_view(), name='index'),
    path('home', views.Normal.as_view(), name='index'),
    path('auth', views.AuthView.as_view(), name='auth'),
    path('test', views.Authentication.as_view(), name='test'),
]