from django.shortcuts import render, redirect, get_object_or_404
from inicio.forms import CrearClienteForm, CrearLibroForm, BuscarLibroForm, EditarLibroForm, PortadaForm
from inicio.models import Libro, Cliente
from django.contrib.auth.decorators import login_required
# View para la página de inicio
def inicio(request):
    return render(request, 'inicio/index.html')

# View para crear un libro
@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = CrearLibroForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            libro = Libro(nombre=datos.get('nombre'), genero=datos.get('genero'), precio=datos.get('precio'), fecha_lanzamiento=datos.get('fecha_lanzamiento'), sinopsis=datos.get('sinopsis'))
            libro.save()
            return redirect('/libros') 
    else:
        form = CrearLibroForm()

    return render(request, 'inicio/crear_libro.html', {'form': form})

# View para listar libros
def lista_libros(request):
    formulario = BuscarLibroForm(request.GET)
    # libros = Libro.objects.all() 
    
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        libros = Libro.objects.filter(nombre__icontains=nombre)
    
    return render(request, 'inicio/lista_libros.html', {'libros': libros, 'formulario': formulario})


# View para eliminar libros
@login_required
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    
    return redirect('/libros')

#View para editar libros
@login_required
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    
    form = EditarLibroForm(initial={'nombre': libro.nombre, 'genero': libro.genero,'precio': libro.precio, 'fecha_lanzamiento': libro.fecha_lanzamiento, 'sinopsis': libro.sinopsis})
    
    if request.method == 'POST':
        form = EditarLibroForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            
            libro.nombre = datos['nombre']
            libro.genero = datos['genero']
            libro.precio = datos['precio']
            libro.fecha_lanzamiento = datos['fecha_lanzamiento']
            libro.sinopsis = datos['sinopsis']
            libro.save()
            return redirect('ver_libro', id=libro.id)
        
    return render(request, 'inicio/editar_libro.html', {'form': form, 'libro': libro})

def ver_libro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, 'inicio/ver_libro.html', {'libro': libro})

def portada(request, id):
    libro = Libro.objects.get(id=id)

    if request.method == 'POST':
        form = PortadaForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('ver_libro', id=libro.id)
    else:
        form = PortadaForm(instance=libro)
   
    return render(request, 'inicio/portada.html', {'libro': libro, 'form_portada': form})    


def about_me(request):
    return render (request, 'inicio/about_me.html')



# # View para crear un cliente
# @login_required
# def crear_cliente(request):
#     if request.method == 'POST':
#         form = CrearClienteForm(request.POST)
#         if form.is_valid():
#             datos = form.cleaned_data
#             cliente = Cliente(nombre=datos.get('nombre'), direccion=datos.get('direccion'), telefono=datos.get('telefono'))
#             cliente.save()
#             return redirect('/clientes') 
#     else:
#         form = CrearClienteForm()

#     return render(request, 'inicio/crear_cliente.html', {'form': form})


# # View para listar clientes
# def lista_clientes(request):
#     clientes = Cliente.objects.all()
#     return render(request, 'inicio/lista_clientes.html', {'clientes': clientes})