from django.contrib import admin
from django.urls import path
from learnDjango import views
urlpatterns = [
    #path("{urlpath}",{view class}, name="{reverse indexing}")
    path('', views.Index.as_view(), name='index'),
    path('index', views.Index.as_view(), name='index'),
    path('login', views.Login_view.as_view(), name='login'),
    path('logout', views.Logout_view.as_view(), name='logout'),
    path('payment', views.Payment_view.as_view(), name='payment'),

]