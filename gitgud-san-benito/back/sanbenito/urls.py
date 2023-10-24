from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .models import *
from .views import *

post_router = DefaultRouter()
post_router.register(r'ver_carabineros', VerCarabineros)
post_router.register(r'ver_inspectores', VerInspectores)
post_router.register(r'ver_infractores', VerInfractores)
post_router.register(r'ver_infracciones', VerInfracciones)
post_router.register(r'ver_evidencia', VerEvidencia)