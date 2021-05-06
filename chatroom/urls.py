from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('create_room',views.create_room,name = 'create_room'),
    path('join_room',views.join_room,name='join_room'),
    path('chatpage/<str:room_name>/<str:username>',views.chatpage,name='chatpage')
]
