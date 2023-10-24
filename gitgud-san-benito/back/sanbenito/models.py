from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.utils import timezone
from django.db import models

# Modelo base de una persona
class Persona(models.Model):
    nombres = models.CharField(max_length=255, null=True)
    apellidos = models.CharField(max_length=255, null=True)
    rut = models.IntegerField(max_length=9, primary_key=True)  # Aquí estamos usando un campo CharField para representar el RUT
    fecha_de_nacimiento = models.DateField(default=timezone.now, null=False)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"

# Personas encargadas de emitir los partes
class Carabinero(models.Model):
    rango = models.CharField(max_length=50, null=True)

class Inspector(models.Model):
    area_de_inspeccion = models.CharField(max_length=100, null=True)

# Persona que comete una infraccion
class Infractor(models.Model):
    numero_de_infracciones = models.PositiveIntegerField(default=0)

# Persona que juzga el estado de una infraccion
class Juez(models.Model):
    experiencia_judicial = models.PositiveIntegerField(default=0)

# El ticket generado por un carabinero o inspector hacia un infractor
class Infraccion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_emision = models.DateField()
    gravedad = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    acusado = models.CharField(max_length=9)  # RUT del infractor
    acusante = models.CharField(max_length=9)  # RUT del carabinero o inspector
    patente_auto = models.CharField(max_length=10)
    multa = models.IntegerField()

    def __str__(self):
        return f"Infracción ID: {self.id} - Acusado: {self.acusado} - Acusante: {self.acusante}"

# Documento que contiene la evidencia de una infraccion
class Evidencia(models.Model):
    id = models.AutoField(primary_key=True)
    acusado = models.IntegerField()
    descripcion = models.IntegerField()
