from django import forms
from .models import Libro

class LibroFormBase(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30) 
    precio = forms.CharField(max_length=20)

class CrearLibroForm(LibroFormBase):
    fecha_lanzamiento = forms.DateField()
    sinopsis = forms.CharField(max_length=2000)
    
class EditarLibroForm(LibroFormBase):
    fecha_lanzamiento = forms.DateField()
    sinopsis = forms.CharField(max_length=2000)


class BuscarLibroForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)

class PortadaForm(forms.ModelForm):
    portada = forms.ImageField(required=False, widget=forms.FileInput) 
    class Meta:
        model = Libro
        fields = ['portada']
#-----------------------------------------------------------------------------------

class CrearClienteForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20)
