from rest_framework import viewsets
from .serializer import RegistroSerializer  # Serializer de registro por cedula
from .serializer import RegistroSerializersearch  # Serializer de registro por estado, municipio y parroquia
from .models import RegistroElectoral
from apps.centro_votacion.models import CentroVotacion


class RegistroViewSet(viewsets.ModelViewSet):
    """ Clase para para la busqueda por cedula"""
    serializer_class = RegistroSerializer
    queryset = RegistroElectoral.objects.all().order_by('cedula')


class RegistroViewSetsearch(viewsets.ModelViewSet):
    """ Clase para para la busqueda por estado, municipio y parroquia, (Centros de votacion)"""
    serializer_class = RegistroSerializersearch
    queryset = CentroVotacion.objects.all().order_by('id','cod_n')

