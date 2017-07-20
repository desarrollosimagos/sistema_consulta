# -*- encoding: utf-8 -*-# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.centro_votacion.models import CentroVotacion
from .models import RegistroElectoral
from .forms import FormElector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
##############################################################################
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.registro.serializer import RegistroSerializer  # Modelo de registro para la busqueda por cedula
from apps.registro.serializer import RegistroSerializersearch  # Modelo para la busqueda por estado, municipio y parroquia
import json
import operator
##############################################################################

# Create your views here.


@login_required(login_url='/iniciar/login/')
def RegistrarElector(request):  # Forma actual
    """
        Función para registrar un elector
    """
    estados = Estado.objects.all()
    municipios = Municipio.objects.all()
    parroquias = Parroquia.objects.all()
    centros = CentroVotacion.objects.all()

    if request.method == 'POST':
        from_regelector = FormElector(request.POST, request.FILES)
        if from_regelector.is_valid():
            nuevo_regelector = from_regelector.save(commit=False)
            nuevo_regelector.user = request.user.username
            nuevo_regelector.s_apellido = request.POST['s_apellido']
            nuevo_regelector.save()
            return HttpResponseRedirect('/registro_electoral/listar_elector')
    else:
        from_regelector = FormElector()
    ctx = {'from_regelector': from_regelector, 'estados': estados, 'municipios': municipios, 'parroquias': parroquias, 'centros': centros}  #  ctx = Contexto (datos de los modelos)
    return render_to_response('registroElectoral/elector.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarElector(request,pk):
    """
        Función para editar los datos de un elector
    """
    estados = Estado.objects.all()
    centros = CentroVotacion.objects.all()
    obj_regelector = RegistroElectoral.objects.get(id=pk)
    f_nac = obj_regelector.f_nac.strftime("%d/%m/%Y")
    municipios = Municipio.objects.filter(estado_id=obj_regelector.cod_estado_id)
    parroquias = Parroquia.objects.filter(estado_id=obj_regelector.cod_estado_id,municipio=obj_regelector.cod_municipio_id)

    if request.method == 'POST':

        form_regelector = FormElector(request.POST, request.FILES, instance=obj_regelector)
        if form_regelector.is_valid():
            edit_regelector = form_regelector.save(commit=False)
            edit_regelector.user = request.user.username
            edit_regelector.s_apellido = request.POST['s_apellido']
            edit_regelector.save()
            return HttpResponseRedirect('/registro_electoral/listar_elector')
    else:
        form_regelector = FormElector(instance=obj_regelector)
    ctx = {'form_regelector': form_regelector, 'obj_regelector': obj_regelector, 'estados': estados, 'municipios': municipios, 'parroquias': parroquias, 'centros': centros, 'f_nac': f_nac}  # ctx = Contexto
    return render_to_response('registroElectoral/edit_elector.html',ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarElector(request,pk):
    """
        Función para eliminar un elector. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.
    """
    obj_regelector = RegistroElectoral.objects.get(id=pk)
    obj_regelector.delete()
    return HttpResponseRedirect('/registro_electoral/listar_elector')


@login_required(login_url='/iniciar/login/')
def BuscarAjaxCentros(request):
    """
        Función para filtar los centros de votación según su estado, municipio y parroquia.
    """
    id_est = request.GET['id_est']
    id_mun = request.GET['id_mun']
    id_parr = request.GET['id_parr']
    centros = CentroVotacion.objects.filter(estado_id=id_est, municipio=id_mun, parroquia=id_parr)
    data = serializers.serialize('json', centros, fields=('cod_n', 'c_votacion'))
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/iniciar/login/')
def ListarElector(request):  # Forma actual
    """
        Función para listar los electores. Se usa 'context_object_name' para enviar los registros del modelo
        a la vista especificada.
    """
    listar_elector = RegistroElectoral.objects.all()
    municipio = Municipio.objects.all()
    parroquia = Parroquia.objects.all()

    ctx = {
        'listar_elector': listar_elector,
        'municipio' : municipio,
        'parroquia' : parroquia,
    }
    return render_to_response('registroElectoral/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
        Función para importar datos de electores a la base de datos mediante un archivo .csv.

        Se usa os.path.dirname(os.path.abspath(__file__)) y os.getcwd() para obtener la ruta del proyecto
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = os.getcwd()

    reader = csv.reader(open(DIR_URL+str("/apps/registro/script/aragua.csv")))

    # Recorrido de los registros del csv
    i = 1
    for row in reader:

        #if  i > 10:
        #    break;
        data = row[0].split(';')
        print "DATOS: ", data
        # Validando el nombre completo----------------------------------
        primer_ape = ""
        segundo_ape = ""
        primer_nombre = ""
        segundo_nombre = ""

        #print "Primer apellido: "+data[2]+" Segundo apellido: "+data[3]+" Primer nombre: "+data[4]+" Segundo nombre: "+data[5]

        i += 1

        # Cargando datos en el modelo
        elector = RegistroElectoral(
            nac=data[0],
            cedula=data[1],
            p_apellido=data[2],
            s_apellido=data[3],
            p_nombre=data[4],
            s_nombre=data[5],
            f_nac=data[6],
            sexo=data[7],
            cod_nuevo=data[11],
            cod_estado_id=data[8],
            cod_municipio=data[9],
            cod_parroquia=data[10],)
        elector.save()
    return HttpResponseRedirect('/registro_electoral/listar_elector')

##############################################################################
#             Clase para capturar datos serializados con viewsets
##############################################################################
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
#import itertools
from itertools import chain
from django import http
from django.http import Http404
from rest_framework import filters


# Clase para validar registro no encontrado
class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'No se encontraron Registros'

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail


# Generacion de la api de registro de centro de votacion (cne)
class RegistroView(generics.ListAPIView):

    model = RegistroElectoral
    serializer_class = RegistroSerializer
    lookup_field = 'cedula'
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('cedula')

    def get_queryset(self):

        cedula = self.kwargs['cedula']

        if cedula is not None:
            queryset = RegistroElectoral.objects.all()
            queryset = queryset.filter(cedula=cedula)


            if queryset.exists():

                return queryset
            else:
		raise NotFound()

################################################################

# Generacion de la api de registro de centro de votacion (cne)
class RegistroViewSearch(generics.ListAPIView):

    model = RegistroElectoral
    serializer_class = RegistroSerializersearch
    #lookup_field = 'cedula'
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('cedula')

    def get_queryset(self):

        estado = self.kwargs['estado']
	municipio = self.kwargs['municipio']
	parroquia = self.kwargs['parroquia']

        if estado is not None and municipio is not None and parroquia is not None:
            queryset = CentroVotacion.objects.all()
            queryset = queryset.filter(estado_id=estado,municipio=municipio,parroquia=parroquia)


            if queryset.exists():

                return queryset
            else:
		raise NotFound()
