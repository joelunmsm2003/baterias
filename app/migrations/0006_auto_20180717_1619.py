# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-17 16:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180717_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='marca',
        ),
        migrations.AddField(
            model_name='produccion',
            name='marca_vehiculo',
            field=models.ForeignKey(blank=True, help_text='Marca del veh\xedculo (p.e. Nissan)', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Vehiculo'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='nombre',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 17, 16, 19, 54, 885584), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]