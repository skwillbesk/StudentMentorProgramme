from django.urls import path
from . import views

urlpatterns = [
	
	path('chats/',views.chats,name = 'chats'),
	path('chat/<int:pk>/',views.chat,name = 'chat'),
]

