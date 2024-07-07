from django.db import models
from datetime import date
# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20) 
    precio = models.CharField(max_length=20)  
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    fecha_lanzamiento = models.DateField(default=date.today)
    sinopsis = models.CharField(max_length=2000, default='No se ha creado una sinopsis para este libro')
    def __str__(self):
        return f'Libro: {self.nombre}'
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'Cliente: {self.nombre} \n Direccion: {self.direccion} \n Telefono: {self.telefono}'
