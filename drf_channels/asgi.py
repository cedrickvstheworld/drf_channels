"""
ASGI config for drf_channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import DRFChannelsAPI.urls

# from channels.auth import AuthMiddlewareStack
from DRFChannelsAPI.middlewares import JwtAuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_channels.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AllowedHostsOriginValidator(
      JwtAuthMiddlewareStack(
        URLRouter(DRFChannelsAPI.urls.websocket_urlpatterns),
      ),
    ),
})
