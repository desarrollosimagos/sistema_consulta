from django.conf.urls import patterns, url
from apps.centro_votacion.views import RegistrarCentroVotacion, ActualizarCentroVotacion, EliminarCentroVotacion, ListarCentroVotacion, BuscarAjax, load_data # Importamos las Vistas de centro de votacion

# URL para Centro de Votacion
urlpatterns = [
    url(r'^registrar_centro/', 'apps.centro_votacion.views.RegistrarCentroVotacion', name="registrar_centro",),
    url(r'^actualizar_centro/(?P<pk>\d+)/$', 'apps.centro_votacion.views.ActualizarCentroVotacion', name='actualizar_centro',),
    url(r'^eliminar_centro/(?P<pk>\d+)/$', 'apps.centro_votacion.views.EliminarCentroVotacion', name='eliminar_centro',),
    url(r'^listar_centro_votacion/$','apps.centro_votacion.views.ListarCentroVotacion', name='listar_centro_votacion',),
    url(r'^busquedaajax/$','apps.centro_votacion.views.BuscarAjax'),
    url(r'^data/', 'apps.centro_votacion.views.load_data', name="datos_municipio",), # URL de Exportacion para la data
]
