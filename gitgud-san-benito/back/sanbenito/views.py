from django.shortcuts import render
from django.http import HttpResponse
from .models import Infraccion

# Muestra la pagina principal de backend
def index(request):
    return render(request,"index.html")

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
