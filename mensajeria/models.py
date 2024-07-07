from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.emisor} -> {self.receptor}: {self.contenido}'

class MensajeGeneral(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario}: {self.contenido}'
