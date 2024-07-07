from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormCreacion, FormEditarPerfil, FormCambiarAvatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra
# Create your views here.

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            
            django_login(request, user)

            DatosExtra.objects.get_or_create(user=user)

            return redirect('inicio')

    return render(request, 'usuarios/login.html', {'formulario': formulario})

def signup(request):
    
    formulario = FormCreacion()
    
    if request.method == "POST":
        formulario = FormCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'usuarios/signup.html', {'formulario': formulario})

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'usuarios/perfil.html', {'usuario': usuario})



@login_required
def editar_perfil(request):
    
    formulario = FormEditarPerfil(initial={'avatar': request.user.datosextra.avatar},instance=request.user)
    
    if request.method == 'POST':
        formulario = FormEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            request.user.datosextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.datosextra.save()
            formulario.save()
            return redirect('editar_perfil')
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')
    form = ...
    
@login_required
def cambiar_avatar(request):
    usuario = request.user
    datos_extra, created = DatosExtra.objects.get_or_create(user=usuario)
    
    if request.method == 'POST':
        form = FormCambiarAvatar(request.POST, request.FILES, instance=datos_extra)
        if form.is_valid():
            form.save()
            return redirect('cambiar_avatar')
    else:
        form = FormCambiarAvatar(instance=datos_extra)
    
    return render(request, 'usuarios/avatar.html', {'formulario_de_avatar': form})

