from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import DatosExtra


class FormCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasena', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {key: '' for key in fields}

class FormEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False, widget=forms.FileInput) 
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar',] 

class FormCambiarAvatar(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput) 
    
    class Meta:
        model = DatosExtra
        fields = ['avatar']