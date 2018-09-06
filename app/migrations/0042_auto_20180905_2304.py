# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-05 23:04
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0041_auto_20180905_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='usuario',
            field=models.ForeignKey(blank=True, help_text='Modelo del veh\xedculo ', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_modelo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 5, 23, 4, 20, 918795), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]
