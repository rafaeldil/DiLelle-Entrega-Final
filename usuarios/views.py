from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            ...
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})