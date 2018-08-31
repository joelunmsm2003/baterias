from django.db import models
from  app.models import *
import pandas as pd
datos=pd.read_csv('http://xiencias.com:/home/baterias/MarcasModelosBaterias.csv',header=0)
print (datos)
mo=datos['MARCA']
ma=datos['MODELO ']


Bateria.objects.all().delete()

for _mo in mo:
	Bateria(marca=_mo).save()

for _ma in ma:
	Bateria(modelo=_ma).save()