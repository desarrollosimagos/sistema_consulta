from django.forms import ModelForm
from django import forms
from apps.registro.models import RegistroElectoral

class FormElector(ModelForm):
    class Meta:
        model = RegistroElectoral
        exclude = {'user','s_apellido'}
