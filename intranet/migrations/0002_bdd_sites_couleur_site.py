# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-02-25 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdd_sites',
            name='couleur_site',
            field=models.CharField(default=' ', max_length=400),
        ),
    ]
