from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    chef_equipe = models.CharField(max_length=100)
    projet_en_cours = models.CharField(max_length=150, blank=True, null=True)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - Chef: {self.chef_equipe}"
