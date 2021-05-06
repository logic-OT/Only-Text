from django.urls import path
from .consumers import chat

ws_urls = [

 	path('chatpage/<str:room_name>/<str:username>',chat.as_asgi())

]