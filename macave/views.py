from django.shortcuts import render, get_object_or_404
from .models import Vin


# Create your views here.
def cave(request):
    return render(request, 'macave/cave.html', {})


def vins(request):
    vins = Vin.objects.order_by('published_date')
    return render(request,'macave/vins.html', {'vins':vins})


def vin_detail(request, pk):
    vin = get_object_or_404(Vin, pk=pk)
    return render(request, 'macave/vin_detail.html', {'vin': vin})


def accueil(request):
    return render(request, 'macave/../templates/accueil.html', {})