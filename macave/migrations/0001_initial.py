# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('region', models.CharField(max_length=20)),
                ('commentaire', models.TextField()),
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
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(to='macave.Region', blank=True)),
            ],
        ),
    ]
