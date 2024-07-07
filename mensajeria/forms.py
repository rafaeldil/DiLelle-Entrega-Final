from django import forms
from .models import Mensaje, MensajeGeneral

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']

class MensajeGeneralForm(forms.ModelForm):
    class Meta:
        model = MensajeGeneral
        fields = ['contenido']
