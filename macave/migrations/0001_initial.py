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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom_pays', models.CharField(unique=True, max_length=20)),
                ('commentaire', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom_region', models.CharField(unique=True, max_length=20)),
                ('commentaire', models.TextField()),
                ('nom_pays', models.ForeignKey(default='nil', blank=True, to='macave.Pays', to_field='nom_pays')),
            ],
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom_vin', models.CharField(max_length=50)),
                ('etiquette', models.CharField(max_length=30)),
                ('millesime', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('nom_region', models.ForeignKey(default='nil', blank=True, to='macave.Region', to_field='nom_region')),
            ],
        ),
    ]
