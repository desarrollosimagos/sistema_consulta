from rest_framework import viewsets
from .serializers import CentroVotacionSerializer
from .models import CentroVotacion

class CentroVotacionViewSet(viewsets.ModelViewSet):
    serializer_class = CentroVotacionSerializer
    queryset         = CentroVotacion.objects.all()
