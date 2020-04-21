from django.urls import path
from . import views

urlpatterns = [
    path('', views.question),
    path('question/', views.question, name='simple-qa-question'),
    path('answer/', views.answer, name='simple-qa-answer'),
]
