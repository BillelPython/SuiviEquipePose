from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_equipes, name='liste_equipes'),
]
