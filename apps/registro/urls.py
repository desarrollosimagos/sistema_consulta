# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarElector, RegistrarElector, ActualizarElector, EliminarElector, BuscarAjaxCentros, RegistroView, RegistroViewSearch

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_elector/$', 'apps.registro.views.ListarElector', name="listar_elector",),
    url(r'^registrar_elector/', 'apps.registro.views.RegistrarElector', name="registrar_elector",),
    url(r'^actualizar_elector/(?P<pk>\d+)/$', 'apps.registro.views.ActualizarElector', name="actualizar_elector",),
    url(r'^eliminar_elector/(?P<pk>\d+)/$', 'apps.registro.views.EliminarElector', name="eliminar_elector",),
    url(r'^busqueda_ajax_centros/$', 'apps.registro.views.BuscarAjaxCentros', name='listar_centros',),
    url(r'^cedula=(?P<cedula>\d+)$', RegistroView.as_view(), name="list_registro",),
    url(r'^estado=(?P<estado>\d+)&municipio=(?P<municipio>\d+)&parroquia=(?P<parroquia>\d+)$', RegistroViewSearch.as_view(), name="list_registro_search",),
    url(r'^data/', 'apps.registro.views.load_data', name="datos_electores",), # URL de Importación para la data
]
