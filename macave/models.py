from django.db import models
from django.utils import timezone


# Create your models here.
class Vin(models.Model):
    author = models.ForeignKey('auth.User')
    nom = models.CharField(max_length=50)
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


class Region(models.Model):
    nom = models.CharField(max_length=20)
    commentaire = models.TextField()

    def __str__(self):
        return self.nom

