from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil/editar/password', views.CambiarPassword.as_view(), name = 'cambiar_pass'),
]
