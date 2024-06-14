from django.shortcuts import render
from inicio.forms import CrearClienteForm, CrearLibroForm
from inicio.models import Libro, Cliente

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')


def crear_libro(request):
    if request.method == 'POST':
        form =  CrearLibroForm
        if form.is_valid():
            datos = form.cleaned_data
            libro = Libro(nombre=datos.get('nombre'), genero=datos.get('genero'), precio=datos.get('precio'))
            
            
def crear_cliente(request):
    if request.method == 'POST':
        form =  CrearClienteForm
        if form.is_valid():
            datos = form.cleaned_data
            cliente = Cliente(nombre=datos.get('nombre'), direccion=datos.get('direccion'), precio=datos.get('numero'))