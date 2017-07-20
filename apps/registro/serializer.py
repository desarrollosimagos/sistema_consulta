#encoding:utf-8
from rest_framework import serializers
from .models import RegistroElectoral
from apps.topologia.estados.serializers import EstadoSerializer
from apps.topologia.municipios.serializers import MunicipioSerializer
from apps.topologia.parroquias.serializers import ParroquiaSerializer
from apps.centro_votacion.serializers import CentroVotacionSerializer
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.centro_votacion.models import CentroVotacion
import unicodedata

class RegistroSerializer(serializers.ModelSerializer):
    #cod_estado = EstadoSerializer(many=False, read_only=True)   # Relacion a Estado
    #cod_municipio = MunicipioSerializer(many=False, read_only=True)   # relacion a Municipio
    #cod_parroquia = ParroquiaSerializer(many=False, read_only=True)   # relacion a Municipio
    nom_parroquia = serializers.SerializerMethodField('calculo_cod_parr')  # Metodo para arrojar el string de parroquia
    nom_mun = serializers.SerializerMethodField('calculo_cod_mun')  # Metodo para arrojar el string de municipio
    nom_estado = serializers.SerializerMethodField('calculo_cod_est')  # Metodo para arrojar el string de estado
    c_votacion = serializers.SerializerMethodField('calculo_centro_votacion')  # Metodo para arrojar el string de centro_votacion
    c_direccion = serializers.SerializerMethodField('calculo_centro_votacion_dir')  # Metodo para arrojar el string de la direccion
    f_nac = serializers.SerializerMethodField('format_fecha')  # Metodo para arrojar la fecha formatead en español
    sexo = serializers.SerializerMethodField('format_sexo')  # Metodo para formatear el campo sexo
    p_apellido = serializers.SerializerMethodField('null_p_apellido')  # Metodo para validar campo null p_apellido
    s_apellido = serializers.SerializerMethodField('null_s_apellido')  # Metodo para validar campo null s_apellido
    p_nombre = serializers.SerializerMethodField('null_p_nombre')  # Metodo para validar campo null p_nombre
    s_nombre = serializers.SerializerMethodField('null_s_nombre')

    class Meta:

        model = RegistroElectoral

        fields = (
            'id',
            'cedula',
            'p_apellido',
            's_apellido',
            'p_nombre',
            's_nombre',
            'f_nac',
            'sexo',
            'cod_estado',
            'nom_estado',
            'cod_municipio',
            'nom_mun',
            'cod_parroquia',
            'nom_parroquia',
            'cod_nuevo',
            'c_votacion',
            'c_direccion',)

        #depth = 1  # Forma de reflejar la relacion entre modelos

        def __unicode__(self):
            return self.cod_municipio

    # Metodo para arrojar el string de parroquia
    def calculo_cod_parr(self, obj):
        id_est = obj.cod_estado_id
        id_mun = obj.cod_municipio_id
        id_parr = obj.cod_parroquia_id
        parroquias = Parroquia.objects.filter(municipio=id_mun,estado_id=id_est,cod_parroquia=id_parr)[0].parroquia
        #print "PARROQUIA: ",parroquias
        return unicode(parroquias.replace('\t',''))

    # Metodo para arrojar el string de municipio
    def calculo_cod_mun(self, obj):
        id_est = obj.cod_estado_id
        id_mun = obj.cod_municipio_id
        municipios = Municipio.objects.filter(cod_municipio=id_mun,estado_id=id_est)[0].municipio
        return unicode(municipios.replace('\t',''))

    # Metodo para arrojar el string de estado
    def calculo_cod_est(self, obj):
        id_est = obj.cod_estado_id
        estado = Estado.objects.filter(cod_estado=id_est)[0].estado
        #print "estado: ",estado
        return unicode(estado.replace('\t',''))

    # Metodo para arrojar el string de centro_votacion
    def calculo_centro_votacion(self, obj):
        id_est = obj.cod_estado_id
        id_mun = obj.cod_municipio_id
        id_parr = obj.cod_parroquia_id
        id_cod_n = obj.cod_nuevo_id
        centro = CentroVotacion.objects.filter(municipio=id_mun,estado_id=id_est,parroquia=id_parr,cod_n=id_cod_n)[0].c_votacion
        #print "centro: ",centro
        return unicode(centro.replace('\t',''))

    # Metodo para arrojar el string de direccion
    def calculo_centro_votacion_dir(self, obj):
        id_est = obj.cod_estado_id
        id_mun = obj.cod_municipio_id
        id_parr = obj.cod_parroquia_id
        id_cod_n = obj.cod_nuevo_id
        centro = CentroVotacion.objects.filter(municipio=id_mun,estado_id=id_est,parroquia=id_parr,cod_n=id_cod_n)[0].direccion
        #print "centro: ",centro
        return unicode(centro.replace('\t',''))

    # Metodo para arrojar la fecha formatead en español
    def format_fecha(self, obj):
        fecha = ''
        if str(obj.f_nac) != "None":
            fecha = str(obj.f_nac.strftime("%d/%m/%Y")) 
        return fecha

    # Metodo para formatear el campo sexo
    
    def format_sexo(self, obj):
    
        print "SEXO: ",obj.sexo
        sexo = ""
        if obj.sexo == 'M':
            sexo = 'Masculino'
        if obj.sexo == 'F':
            sexo = 'Femenino'
        return sexo

    # Metodo para validar campo null p_apellido
    def null_p_apellido(self, obj):
        p_apellido = ""		
        if unicode(obj.p_apellido) == 'None':
            p_apellido = ""
        else:
            p_apellido = unicode(obj.p_apellido)
        return p_apellido.replace('\t','')

    # Metodo para validar campo null s_apellido
    def null_s_apellido(self, obj):
        s_apellido = ""
        if unicode(obj.s_apellido) == 'None':
            s_apellido = ""
        else:
            s_apellido = unicode(obj.s_apellido)
        return s_apellido.replace('\t','')

    # Metodo para validar campo null p_nombre
    def null_p_nombre(self, obj):
        p_nombre = ""
        if unicode(obj.p_nombre) == 'None':
            p_nombre = ""
        else:
            p_nombre = unicode(obj.p_nombre)
        return p_nombre.replace('\t','')

    # Metodo para validar campo null null_s_nombre
    def null_s_nombre(self, obj):
        s_nombre = ""
        if unicode(obj.s_nombre) == 'None':
            s_nombre = ""
        else:
            s_nombre = unicode(obj.s_nombre)
        return s_nombre.replace('\t','')


# Clase para arrojar la data mediante estado, municipio y parroquia

class RegistroSerializersearch(serializers.ModelSerializer):

    n_estado = serializers.SerializerMethodField('f_estado')  # Metodo para reflejar el string de estado
    n_municipio = serializers.SerializerMethodField('f_municipio')  # Metodo para reflejar el string de municipio
    n_parroquia = serializers.SerializerMethodField('f_parroquia')  # Metodo para reflejar el string de parroquia

    class Meta:

        model = CentroVotacion

        fields = (
            'id',
            'estado',
            'n_estado',
            'municipio',
            'n_municipio',
            'parroquia',
            'n_parroquia',
            'cod_n',
            'cod_v',
            'c_votacion',
            'direccion',
            )

        def __unicode__(self):
            return self.c_votacion

    # Metodo para reflejar el string de estado
    def f_estado(self, obj):
        id_est = obj.estado_id
        n_estado = Estado.objects.filter(cod_estado=id_est)[0].estado
        return unicode(n_estado)

    # Metodo para reflejar el string de municipio
    def f_municipio(self, obj):
        id_est = obj.estado_id
        id_mun = obj.municipio
        municipios = Municipio.objects.filter(cod_municipio=id_mun,estado_id=id_est)[0].municipio
        return unicode(municipios)

    # Metodo para reflejar el string de parroquia
    def f_parroquia(self, obj):
        id_est = obj.estado_id
        id_mun = obj.municipio
        id_parr = obj.parroquia
        parroquias = Parroquia.objects.filter(municipio=id_mun,estado_id=id_est,cod_parroquia=id_parr)[0].parroquia
        return unicode(parroquias)

