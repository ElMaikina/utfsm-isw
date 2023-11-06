from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.utils import timezone
from django.db import models

class Carabinero(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombres = models.CharField(max_length=255, null=True)
    apellidos = models.CharField(max_length=255, null=True)
    fecha_de_nacimiento = models.DateField(default=timezone.now, null=False)
    rango = models.CharField(max_length=50, null=True)

    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f"{self.nombres} {self.apellido}"

class Inspector(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombres = models.CharField(max_length=255, null=True)
    apellidos = models.CharField(max_length=255, null=True)
    fecha_de_nacimiento = models.DateField(default=timezone.now, null=False)
    area_de_inspeccion = models.CharField(max_length=100, null=True)
    
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.nombres} {self.apellido}"

class Infractor(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombres = models.CharField(max_length=255, null=True)
    apellidos = models.CharField(max_length=255, null=True)
    fecha_de_nacimiento = models.DateField(default=timezone.now, null=False)
    numero_de_infracciones = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"

class Juez(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombres = models.CharField(max_length=255, null=True)
    apellidos = models.CharField(max_length=255, null=True)
    fecha_de_nacimiento = models.DateField(default=timezone.now, null=False)
    experiencia_judicial = models.PositiveIntegerField(default=0)

    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"

class Infraccion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_emision = models.DateField()
    gravedad = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    acusado = models.CharField(max_length=12)
    acusante = models.CharField(max_length=12)
    patente_auto = models.CharField(max_length=10)
    multa = models.IntegerField()

    def __str__(self):
        return f"Infracción ID: {self.id} - Acusado: {self.acusado} - Acusante: {self.acusante}"

class Evidencia(models.Model):
    id = models.AutoField(primary_key=True)
    acusado = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='fotos/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
