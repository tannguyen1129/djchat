from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
import chatapp.consumers

websocket_urlpatterns = [
    path('ws/chat/', chatapp.consumers.ChatConsumer.as_asgi()),
]