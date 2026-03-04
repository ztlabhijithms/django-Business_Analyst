from django.urls import re_path
from .consumers import BusinessConsumer

websocket_urlpatterns = [
    re_path(r"ws/business/$", BusinessConsumer.as_asgi()),
]