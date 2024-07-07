from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje, MensajeGeneral
from .forms import MensajeForm, MensajeGeneralForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def enviar_mensaje(request, receptor_id):
    receptor = User.objects.get(id=receptor_id)
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.receptor = receptor
            mensaje.save()
            return redirect('perfil') 
    else:
        form = MensajeForm()
    
    return render(request, 'mensaje_enviar.html', {'form': form, 'receptor': receptor})

@login_required
def chat_general(request):
    if request.method == 'POST':
        form = MensajeGeneralForm(request.POST)
        if form.is_valid():
            mensaje_general = form.save(commit=False)
            mensaje_general.usuario = request.user
            mensaje_general.save()
            return redirect('chat_general')
    else:
        form = MensajeGeneralForm()
    
    mensajes = MensajeGeneral.objects.all().order_by('-fecha_envio')
    return render(request, 'chat_general.html', {'form': form, 'mensajes': mensajes})


