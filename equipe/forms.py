from django import forms
from .models import Equipe , Evaluation

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['franchise','nom', 'chef_equipe', 'nombre_poseurs', 'telephone']


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['affectation', 'ponctualite', 'qualite_travail', 'respect_client', 'commentaire']
        widgets = {
            'affectation': forms.Select(attrs={'class': 'form-select'}),
            'ponctualite': forms.Select(attrs={'class': 'form-select'}),
            'qualite_travail': forms.Select(attrs={'class': 'form-select'}),
            'respect_client': forms.Select(attrs={'class': 'form-select'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

