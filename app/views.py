#    ___       ___       ___       ___            ___       ___   
#   /\  \     /\__\     /\  \     /\__\          /\  \     /\  \  
#  /  \  \   / | _|_   /  \  \   |  L__L        _\ \  \   /  \  \ 
# /  \ \__\ /  |/\__\ / /\ \__\  |   \__\      /\/  \__\ / /\ \__\
# \/\  /  / \/|  /  / \ \/ /  /  /   /__/      \  /\/__/ \ \/ /  /
#   / /  /    | /  /   \  /  /   \/__/          \/__/     \  /  / 
#   \/__/     \/__/     \/__/                              \/__/

# email : joelunmsm@gmail.com
# web   : xiencias.com

print 	 "____   ____                             __________                     "
print 	 "\   \ /   /____    _____   ____  ______ \______   \ ___________ __ __  "
print 	 " \   Y   /\__  \  /     \ /  _ \/  ___/  |     ___// __ \_  __ \  |  \ "
print 	 "  \     /  / __ \|  Y Y  (  <_> )___ \   |    |   \  ___/|  | \/  |  / "
print 	 "   \___/  (____  /__|_|  /\____/____  >  |____|    \___  >__|  |____/  "
print 	 "               \/      \/           \/                 \/           	 "

from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import View
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import Group, User
#from jwt_auth.compat import json
#from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.template import RequestContext
import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd
from django.db.models import Count,Sum
from app.models import *
from app.serializers import *
from django.db.models import Count,Sum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from django.contrib.auth import authenticate
import time
from django.db.models import Func
import os
from datetime import datetime,timedelta,date
import os.path
import requests
import smtplib
from email.mime.text import MIMEText
from django.db.models import Count,Max
import datetime
import random
from django.db.models import Count,Sum
from PIL import Image
from resizeimage import resizeimage
import pandas as pd
from .models import Album
from django.views import generic
import pandas as pd



	
def nuevopaciente(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = PacientesForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Pacientes()

			p = PacientesForm(request.POST, instance=a).save()

			#Atencion(paciente_id=p.id).save()

			#id_a = Atencion.objects.all().values('id').order_by('-id')[0]['id']

			#a = Atencion.objects.get(id=id_a)

			#form = AtencionForm(instance=a)





			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return render(request, 'dashboard.html',{'msj': 'Paciente se guardaron con exito','form':form})



	else:
		form = PacientesForm()

	return render(request, 'dashboard.html',{'form': form})


def login2(request):


	# df=pd.read_csv('/home/baterias/MarcasModelosBaterias.csv',header=0)

	# Bateria.objects.all().delete()


	# for i in range(df.shape[0]):

	# 	marca = df['MARCA'][i]
	# 	modelo = df['MODELO '][i]
	# 	equivalencia = df['EQUIVALENCIA'][i]
	# 	codigo = df['CODIGO'][i]


	# 	Bateria(marca=marca,modelo=modelo,equivalencia=equivalencia,codigo=codigo,).save()


	return render(request, 'login.html',{})

def subir(request):


	df=pd.read_csv('/home/baterias/MarcasModelosBaterias.csv',header=0)

	Bateria.objects.all().delete()


	for i in range(df.shape[0]):

		marca = df['MARCA'][i]
		modelo = df['MODELO '][i]
		equivalencia = df['EQUIVALENCIA'][i]
		codigo = df['CODIGO'][i]


		Bateria(marca=marca,modelo=modelo,equivalencia=equivalencia,codigo=codigo,).save()


	return render(request, 'login.html',{})

def masacre(request):

	
	df=pd.read_csv('/home/baterias/MarcasModelosAutos.csv',header=0)



	Vehiculo.objects.all().delete()
	for i in range(df.shape[0]):

		marca = df['Marca'][i]
		modelo = df['Modelo'][i]
		version = df['Version'][i]
		Vehiculo(nombre=marca,modelo=modelo,version=version,).save()


	return render(request, 'login.html',{})




def ingresar(request):

    username = request.POST['username']
    password = request.POST['password']

    print username,password
    user = authenticate(username=username, password=password)
    if user is not None:

        login(request, user)


        return HttpResponseRedirect('/dashboard/')

    else:


    	return render(request, 'login.html',{'error': 'No existe este usuario'})

 





def guardar(request):

	if request.method == 'POST':

		print 'guardando.......',request.POST
		telefono_1= request.POST['telefono_1']
		telefono_2= request.POST['telefono_2']
		cliente= request.POST['cliente']
		dni= request.POST['dni']
		marca_vehiculo= request.POST['marca_vehiculo']
		modelo= request.POST['modelo']
		version= request.POST['version']
		serie= request.POST['serie']
		anio= request.POST['anio']
		motor= request.POST['motor']
		cilindrada= request.POST['cilindrada']
		color= request.POST['color']
		kilometraje= request.POST['kilometraje']
		placa= request.POST['placa']
		cantidad= request.POST['cantidad']
		marca_producto= request.POST['marca_producto']
		#modelo_bateria= request.POST['modelo']
		precio= request.POST['precio']
		descuento= request.POST['descuento']
		precio_total= request.POST['precio_total']
		cantidad_bu= request.POST['cantidad_bu']
		fecha_atencion=request.POST['fecha_atencion']
		direccion_atencion= request.POST['direccion_atencion']
		referencia= request.POST['referencia']
			#factura
		ruc =request.POST['ruc']
		razon_social=request.POST['razon_social']
		direccion_rs=request.POST['direccion_rs']
		pago= request.POST['comprobante']
		correo= request.POST['correo']
		atiende= request.POST['atiende']
		almacen= request.POST['almacen']
		gmail= request.POST['gmail']
		status= request.POST['status']
		observaciones= request.POST['observaciones']

				#boleta


		nombre_boleta= request.POST['nombre_boleta']
		dni_c= request.POST['dni_c']
		direccion1= request.POST['direccion1']

		



		

		#ruc=ruc,direc_rs=razon_socia,direc_rs=direccion_rs,correo=correo,atiende=atiende,almacen=almacen,gmail=gmail,status=estado,obserbaciones=obserbaciones

        
        

		#ruc = request.POST['ruc']
		Produccion(telefono_1=telefono_1,telefono_2=telefono_2,cliente=cliente,dni=dni,marca_vehiculo_id=None,modelo=modelo,version=version,serie=serie,anio=anio,motor=motor,cilindrada=cilindrada,color=color,kilometraje=kilometraje,placa=placa,cantidad=cantidad,marca_producto=marca_producto,precio=precio,descuento=descuento,precio_total=precio_total,cantidad_bu=cantidad_bu,fecha_atencion=fecha_atencion,direccion_atencion=direccion_atencion,referencia=referencia,comprobante=pago,ruc=ruc,razon_social=razon_social,direccion_rs=direccion_rs,correo=correo,atiende=atiende,almacen=almacen,gmail=gmail,status=status,observaciones=observaciones,nombre_boleta=nombre_boleta,dni_c=dni_c,direccion1=direccion1).save()
		#print 'telefonoooo',tlf1,
	return HttpResponseRedirect("/dashboard")
#referencia=referencia,



def dashboard(request):

	u = User.objects.get(id=request.user.id)

	#grupo =u.groups.get()

	#npacientes = Pacientes.objects.all().count()

	#ncitas = Citas.objects.all().count()

	#natenciones= Atencion.objects.all().count()



	#ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


	
	
	#return render(request, 'dashboard.html',{'user':u,'grupo':grupo,'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})
	return render(request, 'dashboard.html' )


def album(request):

	# u = User.objects.get(id=request.user.id)


	return render(request, 'index.html' )
	
def paciente(request):


	#form = PacientesForm()

	#_pacientes = Pacientes.objects.all()


	#return render(request, 'paciente.html',{'form': form,'pacientes':_pacientes})
	return render(request, 'paciente.html')





def mobile(request):
	"""Return True if the request comes from a mobile device."""
	MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
		return True
	else:
		return False

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]

def traesemana(fecha_inicio):

	id =1

	if Semanas.objects.filter(fecha_inicio__lte=fecha_inicio,fecha_fin__gte=fecha_inicio).count()>0:

		id = Semanas.objects.get(fecha_inicio__lte=fecha_inicio,fecha_fin__gte=fecha_inicio).id

	else:

		id=58

	return id







	
	#Actualiza datos
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)
		telefono = None

		a = Agente.objects.get(user_id=id)

		for i in data:


			data['meta_requerida']=float(str(data['meta_requerida']).replace(',',''))
			data['meta_personal']=float(str(data['meta_personal']).replace(',',''))



			if i=='tipo_agente' :tipo_agente=data['tipo_agente']
			if i=='meta_personal' :a.meta_personal=data['meta_personal']
			if i=='meta_requerida' :a.meta_requerida=data['meta_requerida']
			if i=='correo_capital' :a.correo_capital=data['correo_capital']
			if i=='user__email' :email=data['user__email']
			if i=='photo' :a.photo=data['photo']
			if i=='user__direccion' :a.direccion=data['user__direccion']
			if i=='user__dni' :a.dni=data['user__dni']
			if i=='telefono':a.telefono=data['telefono']
			if i=='telefono_1':a.telefono_1=data['telefono_1']
			if i=='password':
				u = User.objects.get(id=id)
				u.set_password(data['password'])
				u.save()



			if i=='telefono':
				TelefonoUser(user_id=a.user.id,numero=data['telefono']).save()

	
		a.save()



		a= simplejson.dumps('OK')
		return HttpResponse(a, content_type="application/json")

	#Retorna datos del agente
	def get(self, request):



		
		id =request.user.id
		a = Agente.objects.filter(user_id=id).values('user','photo','id','estructura__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','photo','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username','pais__nombre','telefono_1','nivel__nombre','telefono')
		fmt = '%d %b %Y'
		for j in range(len(a)):

			if Agente.objects.get(id=a[j]['id']).fecha_ingreso:
				a[j]['fecha_ingreso'] = Agente.objects.get(id=a[j]['id']).fecha_ingreso.strftime(fmt)
			if Agente.objects.get(id=a[j]['id']).user.nacimiento:
				a[j]['fecha_nacimiento'] = Agente.objects.get(id=a[j]['id']).user.nacimiento

			a[j]['meta_requerida']="{:,}".format(a[j]['meta_requerida'])
			a[j]['meta_personal']="{:,}".format(a[j]['meta_personal'])


		a= simplejson.dumps(ValuesQuerySetToDict(a))
		return HttpResponse(a, content_type="application/json")



