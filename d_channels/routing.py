from django.urls import path
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from app.consumers import BasicConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter(
        [path('', BasicConsumer)]
    ),
})
