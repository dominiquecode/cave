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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom_pays', models.CharField(unique=True, max_length=20)),
                ('commentaire', models.TextField()),
            ],
            options={
                'db_table': 'pays',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom_region', models.CharField(unique=True, max_length=20)),
                ('commentaire', models.TextField()),
                ('nom_pays', models.ForeignKey(to='macave.Pays', to_field='nom_pays', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom_vin', models.CharField(max_length=50)),
                ('etiquette', models.CharField(max_length=30)),
                ('millesime', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('nom_region', models.ForeignKey(to='macave.Region', to_field='nom_region', null=True, blank=True)),
            ],
        ),
    ]
