from django.db import models
from django.utils import timezone

# Si tu veux une liste fixe de franchises
FRANCHISES = [
    ('Alger', 'Sahraoui'),
    ('Oran', 'Trari'),
    ('Constantine', 'Constantine'),
    ('Annaba', 'Kerassa'),
    ('Blida', 'Mouhoubi'),
]

class Equipe(models.Model):
    franchise = models.CharField(
        max_length=100,
        choices=FRANCHISES,
        default='Trari'
    )
    nom = models.CharField(max_length=100)
    chef_equipe = models.CharField(max_length=100)
    nombre_poseurs = models.PositiveIntegerField()
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    numero_commande = models.CharField(max_length=50)
    client = models.CharField(max_length=100)
    date_commande = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.numero_commande} - {self.client}"


class Affectation(models.Model):
    franchise = models.CharField(
        max_length=100,
        choices=FRANCHISES,
        default='Trari'
    )
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    commande = models.CharField(max_length=100)  # Champ à saisir
    nombre_menuiseries = models.PositiveIntegerField(default=0)
    date_affectation = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.equipe.nom} → {self.commande}"



class Evaluation(models.Model):
    affectation = models.ForeignKey('Affectation', on_delete=models.CASCADE)
    date_evaluation = models.DateField(default=timezone.now)
    ponctualite = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Note de 1 à 5")
    qualite_travail = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Note de 1 à 5")
    respect_client = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Note de 1 à 5")
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Évaluation {self.affectation.equipe.nom} - {self.date_evaluation}"

    @property
    def moyenne(self):
        return round((self.ponctualite + self.qualite_travail + self.respect_client) / 3, 2)
