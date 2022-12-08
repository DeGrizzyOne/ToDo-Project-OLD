from django.urls import path
from ToDoListe import views

urlpatterns = [
    path('', views.index),
]