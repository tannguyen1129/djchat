from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

from chatapp.routing import websocket_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chatapp.urls")),
    
    # Web Socket
    path('ws/', include(websocket_urlpatterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)