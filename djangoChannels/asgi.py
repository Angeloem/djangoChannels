import os

from django import setup
# from channels.routing import get_default_application
from django.core.asgi import get_asgi_application

setup()
django_asgi_app = get_asgi_application()


from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoChannels.settings')

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
