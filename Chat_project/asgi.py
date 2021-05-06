"""
WSGI config for Chat_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chatroom.routing import ws_urls

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat_project.settings')

import django
django.setup()


application = ProtocolTypeRouter({
		'http': get_asgi_application(),
		'websocket':AuthMiddlewareStack(URLRouter(ws_urls))
	}) 
