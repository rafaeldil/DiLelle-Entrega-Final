from django.shortcuts import render, redirect
from inicio.forms import CrearClienteForm, CrearLibroForm
from inicio.models import Libro, Cliente

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')


def crear_libro(request):
    if request.method == 'POST':
        form =  CrearLibroForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            libro = Libro(nombre=datos.get('nombre'), genero=datos.get('genero'), precio=datos.get('precio'))
            libro.save()
            
# def crear_cliente(request):
#     if request.method == 'POST':
#         form =  CrearClienteForm(request.POST)
#         if form.is_valid():
#             datos = form.cleaned_data
#             cliente = Cliente(nombre=datos.get('nombre'), direccion=datos.get('direccion'), telefono=datos.get('telefono'))
#             cliente.save()

def crear_cliente(request):
    if request.method == 'POST':
        form = CrearClienteForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cliente = Cliente(nombre=datos.get('nombre'), direccion=datos.get('direccion'), telefono=datos.get('telefono'))
            cliente.save()
            return redirect('inicio') 

    return render(request, 'inicio/crear_cliente.html', {'form': form})

            
def lista_libros(request):
    
    libros = Libro.objects.all()
    
    return render(request, 'inicio/lista_libros.html', {'libros': libros})


def lista_clientes(request):

    clientes = Cliente.objects.all()
    
    return render(request, 'inicio/lista_clientes.html', {'clientes': clientes})
