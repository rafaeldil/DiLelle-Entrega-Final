from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20) 
    precio = models.CharField(max_length=20)  
    def __str__(self):
        return f'Libro: self.nombre \n Genero: self.genero \n Precio: self.precio'
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'Cliente: self.nombre \n Direccion: self.direccion \n Telefono: self.telefono'
