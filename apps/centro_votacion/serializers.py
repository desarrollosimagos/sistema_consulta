from rest_framework.serializers import ModelSerializer
from .models import CentroVotacion # Importamos el modelo Centro de Votacion

class CentroVotacionSerializer(ModelSerializer):
    class Meta:
        model  = CentroVotacion
        fields = ('id', 'estado', 'municipio', 'parroquia', 'c_votacion', 'direccion')
    
    def __unicode__(self):
        return self.parroquia
    
