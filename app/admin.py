from django.contrib import admin
from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from PIL import Image
from resizeimage import resizeimage
import os.path
import json
import requests
from django.contrib import admin
from django.contrib.admin.filters import DateFieldListFilter
import xlwt
from datetime import datetime
import csv



class MyAdminSite(AdminSite):
    site_header = 'POS Administrador'

admin_site = MyAdminSite(name='myadmin')
#admin_site.register(Pos)



# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','modelo')
	list_filter=('nombre',)

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','cliente','dni')
    search_fields=('dni',)

# @admin.register(Modelo_Auto)
# class Modelo_AutoAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     search_fields=('nombre',)


@admin.register(Bateria)
class BateriaAdmin(admin.ModelAdmin):
    list_display = ('id','cantidad','marca','modelo','codigo')
    search_fields=('cantidad',)

@admin.register(Pago)
class PagooAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',)

@admin.register(Atiende)
class AtiendeAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',)

 
@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',)      


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',)



def bulksms(audience):

	url ="http://smsbulk.pe/SmsBulk/rest/ws/bulkSms"
	username = 'xiencias'
	password = '9nG4SB'


	for recipient in audience:
		
		phone_number = recipient

		message = audience[recipient]

		if phone_number[:3] == '+51':

			phone_number = phone_number[1:12]

		else:

			if phone_number[:2] != '51':

				phone_number = '51%s' % phone_number





		params = {'usr' : username,'pas' : password,'msg' : message ,'num' : phone_number}


		print 'params...',params

		reply = requests.get(url, params=params)

		result1 = reply.text

		return result1






