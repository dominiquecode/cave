from django.db import models
from django.utils import timezone


# Create your models here.
class Region(models.Model):
    region = models.CharField(max_length=20, unique=True)
    commentaire = models.TextField()

    def __str__(self):
        return self.region


class Vin(models.Model):
    author = models.ForeignKey('auth.User')
    nom_vin = models.CharField(max_length=50)
    region = models.ForeignKey('Region', 'region', blank=True)
    etiquette = models.CharField(max_length=30)
    millesime = models.IntegerField()
    commentaire = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{0}({1})'.format(self.etiquette, str(self.millesime))
