from django.db import models

# Create your models here.

class Empleado(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nit = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    código_departamento = models.IntegerField()	
    slug = models.SlugField(null=True, blank=True)



