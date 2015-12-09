from django import forms
from .models import Vin


class FormListeVins(forms.Modelform):
    class Meta:
        model = Vin
        fields = ['nom', 'region', 'Region.pays', 'millesime']
