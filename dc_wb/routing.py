from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from posts.consumers import PostConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
    	URLRouter(
    		[
    			path("new/", PostConsumer),
    		]
    	)
    )
})
