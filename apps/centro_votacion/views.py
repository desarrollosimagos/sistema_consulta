# -*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from apps.topologia.estados.models import Estado # Modelo Estado
from apps.topologia.municipios.models import Municipio # Modelo Municipio
from apps.topologia.parroquias.models import Parroquia # modelo Parroquia
from .models import CentroVotacion  # Importamos el modelo centro_votacion
from .forms import CentroVotacionForm # Clase Form Centro votacion
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Paginacion
from django.contrib.auth.decorators import login_required # Forma para impedir el acceso al sistema
from django.core import serializers
import csv
import os
from django.db import connection

#======================================================================================
                           # Metodo RegistrarCentroVotacion
#======================================================================================
@login_required(login_url='/iniciar/login/')
def RegistrarCentroVotacion(request):
    list_estado  = Estado.objects.all() # Modelo de consulta a Estado
    if request.method=='POST':
        form_reg_centro_votacion = CentroVotacionForm(request.POST, request.FILES)
        if form_reg_centro_votacion.is_valid():
            new_reg_centro_votacion = form_reg_centro_votacion.save(commit=False)
            new_reg_centro_votacion.user = request.user.username
            new_reg_centro_votacion.save()
	    return HttpResponseRedirect('/centro_votacion/listar_centro_votacion')
    else:
        form_reg_centro_votacion = CentroVotacionForm()
    ctx = {'form_reg_centro_votacion':form_reg_centro_votacion,'list_estado':list_estado} # ctx = Contexto
    return render_to_response('centro_votacion/registrar_centro_votacion.html',ctx, context_instance=RequestContext(request))

#=====================================================================================
                            # Clase ActualizarCentroVotacion
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def ActualizarCentroVotacion(request,pk):
    obj_reg_cen = CentroVotacion.objects.get(id=pk)
    
    list_estado  = Estado.objects.all()
    #list_mun     = Municipio.objects.all()
    #list_par     = Parroquia.objects.all()
    list_mun     = Municipio.objects.filter(estado_id=obj_reg_cen.estado_id)
    list_par     = Parroquia.objects.filter(estado_id=obj_reg_cen.estado_id,municipio=obj_reg_cen.municipio)

    if request.method=='POST':
        obj_reg_edit_cen = CentroVotacionForm(request.POST, request.FILES, instance=obj_reg_cen)
        if obj_reg_edit_cen.is_valid():
            new_reg_cen = obj_reg_edit_cen.save(commit=False)
            new_reg_cen.user = request.user.username
            new_reg_cen.save()
            return HttpResponseRedirect('/centro_votacion/listar_centro_votacion')
    else:
        obj_reg_edit_cen = CentroVotacionForm(instance=obj_reg_cen)
    ctx = {'obj_reg_edit_cen':obj_reg_edit_cen,'obj_reg_cen':obj_reg_cen,'list_estado':list_estado,'list_mun':list_mun,'list_par':list_par,} # ctx = Contexto
    return render_to_response('centro_votacion/actualizar_centro_votacion.html',ctx, context_instance=RequestContext(request))

#=====================================================================================
                            # Metodo EliminarEstado
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def EliminarCentroVotacion(request,pk):
    obj_reg_cen = CentroVotacion.objects.get(id=pk)
    obj_reg_cen.delete()
    return HttpResponseRedirect('/centro_votacion/listar_centro_votacion')

#======================================================================================
# Metodo para listar Registros y Paginacion
#======================================================================================
@login_required(login_url='/iniciar/login/')
def ListarCentroVotacion(request):
    c_votacion = CentroVotacion.objects.all().order_by('id','estado_id','id_mun','parroquia')
    municipio = Municipio.objects.all()
    parroquia = Parroquia.objects.all()
   
    paginator  = Paginator(c_votacion, 20) # Show 5 contacts per page
    page       = request.GET.get('page')
    try:
        list_centro_votacion = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_centro_votacion = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_centro_votacion = paginator.page(paginator.num_pages)

    array = {
        'list_centro_votacion' : list_centro_votacion,
        'municipio' : municipio,
        'parroquia' : parroquia,
    }
    return render_to_response('centro_votacion/lista_centro_votacion.html', array, context_instance = RequestContext(request))


#======================================================================================
#                         Metodo para la busqueda del pk municipio
#======================================================================================
def BuscarAjax(request):
	id_est     = request.GET['id_est']
	id_mun     = request.GET['id_mun']
	municipios = Municipio.objects.filter(estado_id=id_est,cod_municipio=id_mun)
	for x in municipios:
		id = x.id
		return HttpResponse(id, content_type='application/json')

#======================================================================================
#                                 Url Importar data CSV
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    
    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = os.getcwd()
    
    reader = csv.reader(open(DIR_URL+str("/apps/centro_votacion/script/centros_votacion.csv")))
    
    for row in reader:
        data = row[0].split(';')
        obj_m = Municipio.objects.filter(estado_id=data[0],cod_municipio=data[1])
        for x in obj_m:
        	id_mun = x.id
        centro = CentroVotacion(
            c_votacion      = data[5],
            direccion       = data[6],
            estado_id       = data[0],
            municipio       = data[1],
            parroquia       = data[2],
            id_mun          = id_mun,
            cod_n           = data[3],
            cod_v           = data[4]
            )
        centro.save()
        
    return HttpResponseRedirect('/centro_votacion/listar_centro_votacion')
#======================================================================================
