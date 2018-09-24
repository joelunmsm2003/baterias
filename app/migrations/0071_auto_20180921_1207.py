# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-21 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_auto_20180921_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='distrito',
            field=models.ForeignKey(blank=True, help_text='Distrito', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_nombre', to='app.Distrito'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 12, 7, 47, 562550), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 9, 21, 12, 7, 47, 566067), editable=False, max_length=1000, null=True),
        ),
    ]