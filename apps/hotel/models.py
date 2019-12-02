from django.db import models

# Create your models here.

class Motel(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido =  models.CharField(max_length=50) 
    correo  =  models.EmailField() 
    fecha = models.DateField()

