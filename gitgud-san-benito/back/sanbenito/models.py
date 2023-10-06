from django.db import models

# Create your models here.
class Carabinero(models.Model):
    rut=models.CharField(max_length=7)
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.name
