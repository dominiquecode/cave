from django.forms import Modelform
from .models import Vin

class FormListeVins(Modelform):
    class Meta:
        model = Vin
        fields = ['nom', 'region', 'Region.pays', 'millesime']
