from pyclbr import Class
from wsgiref import validate
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import get_resolver
from django.apps import apps
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status




from . serializer import *
from . models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model, login ,logout
from rest_framework import permissions, status


# Usa el API REST para conectarse con React

# Muestra todos los carabineros
class Carabineros(ModelViewSet):
    queryset = Carabinero.objects.all()
    serializer_class = CarabineroSerial

# Muestra todos los inspectores
class Inspectores(ModelViewSet):
    queryset = Inspector.objects.all()
    serializer_class = InspectorSerial

# Muestra todos los infractores
class Infractores(ModelViewSet):
    queryset = Infractor.objects.all()
    serializer_class = InfractorSerial

# Muestra todos las infracciones
class Infracciones(ModelViewSet):
    queryset = Infraccion.objects.all()
    serializer_class = InfraccionSerial

# Muestra todos las infracciones
class Evidencias(ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerial


