from django.db import models
from django.utils import timezone


# Create your models here.

class Pays(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    commentaire = models.TextField()

    def __str__(self):
        return self.nom


class Region(models.Model):
    region = models.CharField(max_length=20, unique=True)
    commentaire = models.TextField()
    pays = models.ForeignKey('Pays', 'nom', blank=True, default='')

    def __str__(self):
        return self.region


class Vin(models.Model):
    nom = models.CharField(max_length=50)
    region = models.ForeignKey('Region', 'region', blank=True)
    etiquette = models.CharField(max_length=30)
    millesime = models.IntegerField()
    commentaire = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{0}({1})'.format(self.etiquette, str(self.millesime))
