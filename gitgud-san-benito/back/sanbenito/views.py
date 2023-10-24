from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import get_resolver
from django.apps import apps

from . serializer import *
from . models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer

# Usa el API REST para conectarse con React

# Muestra todos los carabineros
class VerCarabineros(ModelViewSet):
    queryset = Carabinero.objects.all()
    serializer_class = CarabineroSerial

# Muestra todos los inspectores
class VerInspectores(ModelViewSet):
    queryset = Inspector.objects.all()
    serializer_class = InspectorSerial

# Muestra todos los infractores
class VerInfractores(ModelViewSet):
    queryset = Infractor.objects.all()
    serializer_class = InfractorSerial

# Muestra todos las infracciones
class VerInfracciones(ModelViewSet):
    queryset = Infraccion.objects.all()
    serializer_class = InfraccionSerial

# Muestra todos las infracciones
class VerEvidencia(ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerial

# Muestra la pagina principal de backend
def index(request):
    print("Bienvenido al Back-End de San Benito!\n")
    
    models = apps.get_models()
    all_views = []

    for key, resolver in get_resolver().reverse_dict.items():
        if isinstance(resolver[0][0], str):
            all_views.append(key)

    # Muestra todos las entidades y sus campos por terminal
    print("Modelos:")
    for model in models:
        print(" - " + model.__name__)
        for campo in model._meta.get_fields():
            print("   - " + campo.name + ": " + campo.__class__.__name__)

    # Muestra todas las vistas por terminal
    print("Vistas:")
    for view in all_views:
        print(" - " + view)

    return render(request, 'index.html', {'models': models, 'all_views': all_views})
    
