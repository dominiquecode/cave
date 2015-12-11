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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom_pays', models.CharField(max_length=20, unique=True)),
                ('commentaire', models.TextField()),
            ],
            options={
                'db_table': 'pays',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom_region', models.CharField(max_length=20, unique=True)),
                ('commentaire', models.TextField()),
                ('nom_pays', models.ForeignKey(null=True, to='macave.Pays', to_field='nom_pays', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom_vin', models.CharField(max_length=50)),
                ('etiquette', models.CharField(max_length=30)),
                ('millesime', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(null=True, auto_now=True)),
                ('nom_region', models.ForeignKey(null=True, to='macave.Region', to_field='nom_region', blank=True)),
            ],
        ),
    ]
