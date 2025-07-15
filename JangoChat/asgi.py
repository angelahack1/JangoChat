# JangoChat/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# This line must come first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JangoChat.settings')

# This line initializes Django
django_asgi_app = get_asgi_application()

# IMPORTANT: Import your app's routing AFTER Django has been initialized
import chat.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})