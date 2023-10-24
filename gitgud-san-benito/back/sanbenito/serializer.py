from rest_framework.serializers import ModelSerializer
from .models import Carabinero
from .models import Inspector
from .models import Infractor
from .models import Juez
from .models import Infraccion
from .models import Evidencia

class CarabineroSerial(ModelSerializer):
    class Meta:
        model = Carabinero
        fields = ['nombres', 'apellidos', 'rut', 'fecha_de_nacimiento', 'rango']  

class InspectorSerial(ModelSerializer):
    class Meta:
        model = Inspector
        fields = ['nombres', 'apellidos', 'rut', 'fecha_de_nacimiento', 'area_de_inspeccion']  

class InfractorSerial(ModelSerializer):
    class Meta:
        model = Infractor
        fields = ['nombres', 'apellidos', 'rut', 'fecha_de_nacimiento', 'numero_de_infracciones']  

class InfraccionSerial(ModelSerializer):
    class Meta:
        model = Infraccion
        fields = ['id', 'fecha_emision', 'gravedad', 'acusado', 'acusante', 'patente_auto', 'multa']  

class EvidenciaSerial(ModelSerializer):
    class Meta:
        model = Evidencia
        fields = ['id', 'acusado', 'descripcion', 'foto', 'video']  

