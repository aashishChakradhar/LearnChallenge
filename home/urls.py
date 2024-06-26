from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('quiz',views.quiz,name='quiz'),
    path('takequiz',views.takequiz,name='takequiz'),
    path('api/get-quiz/',views.get_quiz,name='get_quiz')
]
