from django.conf.urls import include, url
from django.contrib import admin

#urlpatterns = patterns('',
#
#   url(r'^admin/', include(admin.site.urls)),
#
#   url(r'^topologia/',
#   include('apps.topologia.urls')
#                           ),
#                       # PARA AGREGAR LA AUTENTICACION DEL USUARIO
## url(r'^api-auth/',
       # include('rest_framework.urls', namespace='rest_framework')),
#                       url(r'^chaining/',
#                           include('pixelfields_smart_selects.urls')
#                           ),
#
#                       #url(r'^estado/',
#                       #    include('apps.topologia.estados.urls')
#                       #    ),
#
#                       )

urlpatterns = [
    url(r'^administrador/', include(admin.site.urls)),
    url(r'^api/', include('apps.topologia.urls')),
    url(r'^api/', include('apps.centro_votacion.urls')),
    url(r'^', include('apps.registro.urls')),
    # PARA AGREGAR LA AUTENTICACION DEL USUARIO
    #url(r'^api-auth/',
    #    include('rest_framework.urls', namespace='rest_framework')),
    url(r'^chaining/', include('pixelfields_smart_selects.urls')),

    url(r'^estado/', include('apps.topologia.estados.urls')),
    url(r'^', include('apps.topologia.estados.urls')),
    url(r'^municipio/', include('apps.topologia.municipios.urls')),
    url(r'^parroquia/', include('apps.topologia.parroquias.urls')),
    url(r'^centro_votacion/', include('apps.centro_votacion.urls')), # Url para centro de votacion
    url(r'^registro_electoral/', include('apps.registro.urls')), # Url para centro de votacion
    url(r'^iniciar/', include('apps.login.urls')),
]
