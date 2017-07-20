from django.contrib import admin
from apps.registro.models import RegistroElectoral

# Register your models here.
admin.site.register(RegistroElectoral)  # Esto activa en el admin el modelo indicado.
