from django.shortcuts import render, get_object_or_404
from .models import Vin
from .forms import FormListeVins


# Create your views here.
def cave(request):
    return render(request, 'macave/cave.html', {})


def liste_vins(request):
    form_liste_vins = FormListeVins()
    return render(request,'macave/liste_vins.html', {'form_liste_vins':form_liste_vins})


def vin_detail(request, pk):
    vin = get_object_or_404(Vin, pk=pk)
    return render(request, 'macave/vin_detail.html', {'vin': vin})


def accueil(request):
    return render(request, 'accueil.html', {})


def unverre(request):
    return  render(request, 'macave/unverre.html', {})

