from django.contrib import admin
from django.urls import path, include
# from inicio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('productos/', include('productos.urls')),
    path('usuarios/', include('usuarios.urls')),
]
