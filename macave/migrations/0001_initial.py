# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=20)),
                ('commentaire', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('region', models.CharField(unique=True, max_length=20)),
                ('commentaire', models.TextField()),
                ('pays', models.ForeignKey(blank=True, to='macave.Pays', default='', to_field='nom')),
            ],
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom_vin', models.CharField(max_length=50)),
                ('etiquette', models.CharField(max_length=30)),
                ('millesime', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(blank=True, to='macave.Region', to_field='region')),
            ],
        ),
    ]
