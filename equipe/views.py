from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipeForm , EvaluationForm
from django.contrib.auth.decorators import login_required
from .models import Equipe, Affectation , FRANCHISES , Evaluation

@login_required
def liste_equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'equipe/liste_equipes.html', {'equipes': equipes})

@login_required
def ajouter_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_equipes')
    else:
        form = EquipeForm()
    return render(request, 'equipe/ajouter_equipe.html', {'form': form})

@login_required
def modifier_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('liste_equipes')
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'equipe/modifier_equipe.html', {'form': form})

@login_required
def supprimer_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    equipe.delete()
    return redirect('liste_equipes')

def liste_affectations(request):
    affectations = Affectation.objects.select_related('equipe').all()
    return render(request, 'equipe/liste_affectations.html', {'affectations': affectations})


def ajouter_affectation(request):
    equipes = Equipe.objects.all()
    franchises = FRANCHISES

    if request.method == 'POST':
        franchise = request.POST.get('franchise')
        equipe_id = request.POST.get('equipe')
        commande = request.POST.get('commande')
        nombre_menuiseries = request.POST.get('nombre_menuiseries')

        Affectation.objects.create(
            franchise=franchise,
            equipe_id=equipe_id,
            commande=commande,
            nombre_menuiseries=nombre_menuiseries
        )
        return redirect('liste_affectations')

    return render(request, 'equipe/ajouter_affectation.html', {
        'equipes': equipes,
        'franchises': franchises
    })

def ajouter_evaluation(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_evaluations')
    else:
        form = EvaluationForm()
    return render(request, 'ajouter_evaluation.html', {'form': form})

def liste_evaluations(request):
    evaluations = Evaluation.objects.select_related('affectation__equipe')
    return render(request, 'liste_evaluations.html', {'evaluations': evaluations})


