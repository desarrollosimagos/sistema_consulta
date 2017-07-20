from django.forms import ModelForm
from django import forms
from apps.centro_votacion.models import CentroVotacion

class CentroVotacionForm(ModelForm):
    class Meta:
        model   = CentroVotacion
        exclude = {'user',} 