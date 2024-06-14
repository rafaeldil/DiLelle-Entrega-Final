from django import forms

class CrearLibroForm:
    nombre = forms.CharField(max_length=20)
    genero = forms.CharField(max_length=20) 
    precio = forms.CharField(max_length=20)

class CrearClienteForm:
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20)