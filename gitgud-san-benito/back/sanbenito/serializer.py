from rest_framework import serializers
from .models import *

class CarabineroSerial(serializers.ModelSerializer):
    class Meta:
        model = Carabinero
        fields = ['nombres', 'apellidos', 'rut', 'fecha_de_nacimiento', 'rango']  

