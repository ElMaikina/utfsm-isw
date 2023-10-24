from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import get_resolver
from django.apps import apps

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *
from .models import *

# Muestra todas las infracciones cometidas por un mismo infractor
def infracciones_por_infractor(request, rut_infractor):
    infracciones = Infraccion.objects.filter(acusado=rut_infractor)
    return render(request, 'infracciones_por_infractor.html', {'infracciones': infracciones})

# Muestra todas las infracciones emitidas por un mismo acusante
def infracciones_por_acusante(request, rut_acusante):
    infracciones = Infraccion.objects.filter(acusante=rut_acusante)
    return render(request, 'infracciones_por_acusante.html', {'infracciones': infracciones})

# Muestra las infracciones por orden de gravedad
def infracciones_por_gravedad(request):
    infracciones = Infraccion.objects.order_by('-gravedad')
    return render(request, 'infracciones_por_gravedad.html', {'infracciones': infracciones})

# Usa el API REST para conectarse con React

# Muestra todos los carabineros
class VerCarabineros(APIView):
    def get(self, request):
        output = [{'nombres': output.nombres, 
                    'apellidos': output.apellidos, 
                    'rut': output.rut, 
                    'fecha_de_nacimiento': output.fecha_de_nacimiento, 
                    'rango': output.rango}
                  for output in Carabinero.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = CarabineroSerial(data=request.data)
        if serializer.is_valid(raise_execption=True):
            serializer.save()
            return Response(serializer.data)

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
    
