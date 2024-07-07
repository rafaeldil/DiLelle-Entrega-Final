from django.contrib import admin
from django.urls import path, include
from inicio import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear-libro/', views.crear_libro, name='crear_libro'),
    path('libros/', views.lista_libros, name='libros'),
    path('clientes/', views.lista_clientes, name='clientes'), 
    path('eliminar-libro/<int:id>', views.eliminar_libro, name='eliminar_libro'),
    path('editar-libro/<int:id>', views.editar_libro, name='editar_libro'),
    path('ver-libro/<int:id>', views.ver_libro, name='ver_libro'),
    path('portada/<int:id>', views.portada, name='portada'),
]
