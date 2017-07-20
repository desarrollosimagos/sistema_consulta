# -*- encoding: utf-8 -*-
from django.db import models
#from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedForeignKey
from django.core.urlresolvers import reverse
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.centro_votacion.models import CentroVotacion
import datetime
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime

# Create your models here.
NACIONALIDAD = (
    ('V', 'Venezolano'),
    ('E', 'Extranjero'),
)

SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class RegistroElectoral(models.Model):
    
    nac = models.CharField(verbose_name="Nacionalidad", max_length=1, choices=NACIONALIDAD, default='V')
    cedula = models.CharField(verbose_name="Cédula", max_length=8, unique=True, null=True)
    p_apellido = models.CharField(verbose_name="Primer Apellido", max_length=200, null=True)
    s_apellido = models.CharField(verbose_name="Segundo Apellido", max_length=200, null=True)
    p_nombre = models.CharField(verbose_name="Primer Nombre", max_length=200, null=True)
    s_nombre = models.CharField(verbose_name="Segundo Nombre", max_length=200, null=True)
    f_nac = models.DateField('Fecha de nacimiento', null=True)
    sexo = models.CharField(verbose_name="Sexo", max_length=1, choices=SEXO, null=True)
    cod_estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_registro', null=True)
    cod_municipio = models.ForeignKey(Municipio)
    cod_parroquia = models.ForeignKey(Parroquia)
    cod_nuevo = models.ForeignKey(CentroVotacion, to_field='cod_n', on_delete=models.SET_NULL, related_name='centro_registro', null=True)
    cod_viejo = models.CharField(verbose_name="Código anterior", max_length=20, null=True)
    date_create = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    user = models.CharField(max_length=15, null=True)
    mun = models.CharField(max_length=30, null=True)



    def __unicode__(self):
        # Método para retornar por defecto el valor de un campo especificado
        return self.cedula
