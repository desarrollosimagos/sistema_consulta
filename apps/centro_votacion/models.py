# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio # Importamos el Modelo Municipio
from apps.topologia.parroquias.models import Parroquia # Importamos el Modelo Parroquia

# Modelo de Topologia / Centro de Votacion

# Clase de estado
class CentroVotacion(models.Model):
    """Esta es la Clase que define todo lo referente a los Centros de Votacion
        Registrar Modificar Eliminar y Consultar
    """
    estado      = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_centro_votacion', null=True)
    municipio   = models.IntegerField(null=True)
    parroquia   = models.IntegerField(null=True)
    id_mun      = models.IntegerField(null=True)
    cod_n       = models.IntegerField(verbose_name="Cod Nuevo", max_length=11, unique=True, null= True)
    cod_v       = models.CharField(verbose_name="Cod Viejo", max_length=11, unique=False, null= True)
    c_votacion  = models.TextField(max_length=1500, verbose_name='Centro de Votacion')
    direccion   = models.TextField(max_length=1500, verbose_name='Direccion')
    user        = models.CharField(max_length=15, null=True)
    date_create = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    

    def __unicode__(self):
        return self.c_votacion

    def __str(self):
        return self.c_votacion
