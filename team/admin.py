from django.contrib import admin
from .models import Equipe

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'chef_equipe', 'projet_en_cours', 'date_creation')
