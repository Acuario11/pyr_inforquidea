from django.db import models

# Create your models here.
class Orquidea(models.Model):
    tipo_crecimiento= models.CharField(max_length=30, unique=True, null=True)
    nombre_comun=models.CharField(max_length=30, unique=True, null=True)
    floracion=models.CharField(max_length=30, unique=True, null=True)
    duracion_flor=models.CharField(max_length=30, unique=True, null=True)
    tamaño_flor=models.CharField(max_length=30, unique=True, null=True)
    ubicacion=models.CharField(max_length=60, unique=True, null=True)

    def __str__(self):
        return {self.nombre_comun} 
        