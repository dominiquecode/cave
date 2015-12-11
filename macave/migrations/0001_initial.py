# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom_pays', models.CharField(max_length=20, unique=True)),
                ('commentaire', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom_region', models.CharField(max_length=20, unique=True)),
                ('commentaire', models.TextField()),
                ('nom_pays', models.ForeignKey(null=True, to_field='nom_pays', blank=True, to='macave.Pays')),
            ],
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom_vin', models.CharField(max_length=50)),
                ('etiquette', models.CharField(max_length=30)),
                ('millesime', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('nom_region', models.ForeignKey(null=True, to_field='nom_region', blank=True, to='macave.Region')),
            ],
        ),
    ]
