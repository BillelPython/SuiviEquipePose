from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_equipes, name='liste_equipes'),
    path('ajouter/', views.ajouter_equipe, name='ajouter_equipe'),
    path('modifier/<int:equipe_id>/', views.modifier_equipe, name='modifier_equipe'),
    path('supprimer/<int:equipe_id>/', views.supprimer_equipe, name='supprimer_equipe'),

    # Affectations
    path('affectations/', views.liste_affectations, name='liste_affectations'),
    path('affectations/ajouter/', views.ajouter_affectation, name='ajouter_affectation'),

    path('evaluations/', views.liste_evaluations, name='liste_evaluations'),
    path('evaluations/ajouter/', views.ajouter_evaluation, name='ajouter_evaluation'),
]
