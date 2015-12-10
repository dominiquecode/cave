from django.db import models
from django.utils import timezone


# Create your models here.
class Pays(models.Model):
    nom_pays = models.CharField(max_length=20, unique=True)
    commentaire = models.TextField()

    def __str__(self):
        return self.nom_pays


class Region(models.Model):
    nom_region = models.CharField(max_length=20, unique=True)
    commentaire = models.TextField()
    nom_pays = models.ForeignKey('Pays', 'nom_pays', blank=True, default='nil')

    def __str__(self):
        return self.region


class Vin(models.Model):
    nom_vin = models.CharField(max_length=50)
    nom_region = models.ForeignKey('Region', 'nom_region', blank=True, default='nil')
    etiquette = models.CharField(max_length=30)
    millesime = models.IntegerField()
    commentaire = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{0}({1})'.format(self.etiquette, str(self.millesime))
