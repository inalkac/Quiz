from django.urls import path
from . import views

#http://127.0.0.1:8000/quizdb

urlpatterns = [
    path('', views.index, name = 'quizdb'),
    path('<str:category_name>', views.quiz, name = 'quiz'),
    
]