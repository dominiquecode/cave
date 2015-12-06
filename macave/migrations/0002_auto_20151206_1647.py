# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('macave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vin',
            name='commentaire',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vin',
            name='etiquette',
            field=models.CharField(max_length=30),
        ),
    ]
