from django import forms

class CrearLibroForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    genero = forms.CharField(max_length=20) 
    precio = forms.CharField(max_length=20)

class CrearClienteForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20)