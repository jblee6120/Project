from django.urls import path
from .consumers import WSconsumer

websocket_urlpatterns = [
    path('ws/some_url/', WSconsumer.as_asgi()),
    #path('ws/', LoadBooks.as_asgi()),
]