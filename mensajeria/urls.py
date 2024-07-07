from django.urls import path
from . import views

urlpatterns = [
    path('enviar-mensaje/<int:receptor_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('chat-general/', views.chat_general, name='chat_general'),
    # path('mensajes/', views.lista_mensajes, name='lista_mensajes'),
    # path('mensaje/<int:mensaje_id>/', views.ver_mensaje, name='ver_mensaje'),
]
