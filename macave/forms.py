from django import forms
from .models import Vin


class ListeVinsForm(forms.ModelForm):
    class Meta:
        model = Vin
        fields = ['nom_vin', 'nom_region', 'millesime']
