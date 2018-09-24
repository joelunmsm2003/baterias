#    ___       ___       ___       ___            ___       ___   
#   /\  \     /\__\     /\  \     /\__\          /\  \     /\  \  
#  /  \  \   / | _|_   /  \  \   |  L__L        _\ \  \   /  \  \ 
# /  \ \__\ /  |/\__\ / /\ \__\  |   \__\      /\/  \__\ / /\ \__\
# \/\  /  / \/|  /  / \ \/ /  /  /   /__/      \  /\/__/ \ \/ /  /
#   / /  /    | /  /   \  /  /   \/__/          \/__/     \  /  / 
#   \/__/     \/__/     \/__/                              \/__/

# email : joelunmsm@gmail.com
# web   : xiencias.com

print    "____   ____                             __________                     "
print    "\   \ /   /____    _____   ____  ______ \______   \ ___________ __ __  "
print    " \   Y   /\__  \  /     \ /  _ \/  ___/  |     ___// __ \_  __ \  |  \ "
print    "  \     /  / __ \|  Y Y  (  <_> )___ \   |    |   \  ___/|  | \/  |  / "
print    "   \___/  (____  /__|_|  /\____/____  >  |____|    \___  >__|  |____/  "
print    "               \/      \/           \/                 \/              "

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
from app.forms import *
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
from django.contrib.auth.models import User
import datetime
from datetime import datetime,timedelta
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




ahora = datetime.now()
print 'hols_yo soy la hora',ahora

def usuarios(request):
	usuarios = User.objects.all()
	#recetas = Receta.objects.all()
	#context = {'recetas': recetas, 'usuarios':usuarios}
	return render(request, 'header.html', context)


def privado(request):
	usuario = request.user
	context = {'usuario': usuario}
	return render(request, 'header.html', context)
	
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



# @login_required(login_url="/dashboard/")
def vehiculos(request):


	if request.method=='POST':

		form = VehiculosForm(request.POST)
	
		if form.is_valid():

			form.save()

		return HttpResponseRedirect("/dashboard")


	if request.method=='GET':

		vehiculos = Vehiculo.objects.all()
		context = {'datos': vehiculos}
		
		formula = VehiculosForm()

		context = {'datoss': formula}

	return render(request, 'dashboard.html',context)

def login2(request):


	# df=pd.read_csv('/home/baterias/MarcasModelosBaterias.csv',header=0)

	# Bateria.objects.all().delete()


	# for i in range(df.shape[0]):

	#   marca = df['MARCA'][i]
	#   modelo = df['MODELO '][i]
	#   equivalencia = df['EQUIVALENCIA'][i]
	#   codigo = df['CODIGO'][i]


	#   Bateria(marca=marca,modelo=modelo,equivalencia=equivalencia,codigo=codigo,).save()


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
		apellido_p= request.POST['apellido_p']
		apellido_m= request.POST['apellido_m']

		dni= request.POST['dni']
		marca_vehiculo= request.POST['marca_vehiculo']
		modelo= request.POST['modelo']
		version= request.POST['version']
		serie= request.POST['serie']
		anio= request.POST['anio']
		motor= request.POST['motor']
		#cilindrada= request.POST['cilindrada']
		color= request.POST['color']
		kilometraje= request.POST['kilometraje']
		placa= request.POST['placa']
		cantidad= request.POST['cantidad']
		marca_producto= request.POST['marca_producto']

		modelo_bateria= request.POST['modelo']
		precio= request.POST['precio']
		descuento= request.POST['descuento']
		precio_total= request.POST['precio_total']
		cantidad_bu= request.POST['cantidad_bu']
		fecha_atencion=request.POST['fecha_atencion']
		direccion_atencion= request.POST['direccion_atencion']
		distrito=request.POST['distrito']
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
		m_apellido_p= request.POST['m_apellido_p']
		m_apellido_p= request.POST['m_apellido_m']

		dni_c= request.POST['dni_c']
		direccion1= request.POST['direccion1']

		f=str(fecha_atencion).split('/')

		print 'ffffffffffffffffffff', f



		fecha_atencion = datetime.strptime(fecha_atencion, '%d/%m/%Y')

		print 'la FECHA ES CORRECTA???',fecha_atencion

		hora_instalacion= fecha_atencion+timedelta(hours=1)
		print 'Lupita.....', hora_instalacion
		

		#ruc=ruc,direc_rs=razon_socia,direc_rs=direccion_rs,correo=correo,atiende=atiende,almacen=almacen,gmail=gmail,status=estado,obserbaciones=obserbaciones

		
		

		#ruc = request.POST['ruc']
		Produccion(telefono_1=telefono_1,telefono_2=telefono_2,cliente=cliente,apellido_p=apellido_p,apellido_m=apellido_m,dni=dni,marca_vehiculo_id=None,modelo_id=modelo,version=version,serie=serie,anio=anio,motor=motor,color=color,kilometraje=kilometraje,placa=placa,cantidad=cantidad,marca_producto_id=None,precio=precio,descuento=descuento,precio_total=precio_total,cantidad_bu=cantidad_bu,fecha_atencion=fecha_atencion,direccion_atencion=direccion_atencion,referencia=referencia,comprobante=pago,ruc=ruc,razon_social=razon_social,direccion_rs=direccion_rs,correo=correo,atiende=atiende,almacen=almacen,gmail=gmail,status=status,observaciones=observaciones,nombre_boleta=nombre_boleta,dni_c=dni_c,direccion1=direccion1).save()
		#print 'telefonoooo',tlf1,
	return HttpResponseRedirect("/dashboard")
#referencia=referencia,



def dashboard(request):

		if request.method=='POST':
			form = BateriasForm(request.POST)
	
			if form.is_valid():

				form.save()
			return HttpResponseRedirect("/dashboard/")


	
	
		marcas= Vehiculo.objects.values('nombre').annotate(Count('nombre')) #.annotate(Count('nombre')) es para agrupar
		bateria= Bateria.objects.values('marca').annotate(Count('marca'))
		distritos= Distrito.objects.all()
		print'heyyy  aquiir estan los distrito,,...',distritos
		pagos= Pago.objects.all()
		almacen=Almacen.objects.all()
		atiende=Atiende.objects.all()
		status=Status.objects.all()

		nombre=''
		marca=''
		modelos=''
		cliente=""
		marca_b=''
		apellido_p=''
		models=''
		
		apellido_m=''

		dni=''
		telefono_1=''

		telefono_2=''
		models_b=''
		distrito=''
		version=''
		serie=''
		anio=''
		color=''


		kilometraje=''
		placa=''
		cant_ba=''
		cilindrada= ''

		for r in request.GET:

			if r=='marca':

				marca= request.GET['marca']

				modelos = Vehiculo.objects.filter(nombre=marca)

			if r=='marca_b':

				marca_b= request.GET['marca_b']

				print 'yyyyyyyy',marca_b

				models_b = Bateria.objects.filter(marca=marca_b)
				
			if r=='cliente':

				cliente =request.GET['cliente']

			if r=='apellido_p':

				apellido_p =request.GET['apellido_p']

			if r=='apellido_m':

				apellido_m =request.GET['apellido_m']

			if r=='dni':

				dni =request.GET['dni']

			if r=='telefono_1':

				telefono_1 =request.GET['telefono_1']

			if r=='telefono_2':

				telefono_2 =request.GET['telefono_2']

			if r=='distrito':

				distrito =request.GET['ditrito']

			if r=='version': #  NOMBRE DE QUE LE DAS LA url q le das

				version =request.GET['version'] # IDENTIFICADOR / NOMBRE DEL TRAEMODELOS
				print 'quue metraes aca.. VERSIOn...',version

			if r=='serie': 

				serie =request.GET['serie'] 
				print 'quue metraes aca.. SERIEE...',serie


			if r=='anio': 

				anio =request.GET['anio'] 
				print 'por q no e traes el anioo.... ANIOO',anio

			if r=='color': 

				color =request.GET['color'] 
				print '	que color  ke trares......COLOR..	',color


			if r=='cilindrada': #  NOMBRE DE QUE LE DAS LA url q le das

				cilindrada =request.GET['cilindrada'] # IDENTIFICADOR / NOMBRE DEL traemodelos
				print 'cinlidradasssssss...s...',cilindrada




			if r=='kilometraje': #  NOMBRE DE QUE LE DAS LA url q le das

				kilometraje =request.GET['kilometraje'] # IDENTIFICADOR / NOMBRE DEL TRAEM0ODELOS
				print 'quue metraes aca.. kilometraje...',kilometraje

			if r=='placa': #  NOMBRE DE QUE LE DAS LA url q le das

				placa =request.GET['placa'] # IDENTIFICADOR / NOMBRE DEL TRAEMODELOS
				print 'quue placa essss...',placa

			if r=='cant_ba': #  NOMBRE DE QUE LE DAS LA url q le das

				cant_ba =request.GET['cant_ba'] # IDENTIFICADOR / NOMBRE DEL traemodelos
				print 'cantidadessssssssssssssssss...',cant_ba




		v = VehiculosForm()
		baterias=BateriasForm()

		

		return render(request, 'dashboard.html',{'cilindrada':cilindrada,'cant_ba':cant_ba,'placa':placa,'kilometraje':kilometraje,'color':color,'anio':anio,'serie':serie,'version':version,'distrito':distritos,'bateriasform':baterias,'vehiculoform':v,'bateria':bateria,'status':status,'atiende':atiende,'almacen':almacen,'pagos':pagos,'telefono_2':telefono_2,'telefono_1':telefono_1,'dni':dni,'cliente':cliente,'apellido_p':apellido_p,'apellido_m':apellido_m,'modelos':modelos,'marcas':marcas,'marca':marca,'marca_b':marca_b,'marcas_b':models_b})


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



