
from django.conf.urls import  include, url

#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from app.views import *

from django.contrib import admin


admin.site.site_header = 'Baterias al Toque'
from app.admin import admin_site

urlpatterns = [
    
    # url(r'^$', 'views.IndexView'),
    url(r'^admin/', admin.site.urls),
    
    # url(r'^api-token-auth/', 'jwt_auth.views.obtain_jwt_token'),
    url(r'^pos/', admin_site.urls),
    #url(r'api-token-refresh/', refresh_jwt_token),
    url(r'^login/$', login2),
    url(r'^subir/$', subir),
    url(r'^masacre/$', masacre),


    url(r'^ingresar/$',ingresar),
    url(r'^dashboard/$', dashboard),
    url(r'^album/$', album),

    url(r'^paciente/$', paciente),
    url(r'^nuevopaciente/$', nuevopaciente),

    
    #url(r'^enviasms$', Enviasms.as_view()),

]
