# from channels.routing import route
# from chat.consumers import ws_message, ws_add, ws_disconnect
#
# channel_routing = [
#     # route("http.request", "chat.consumers.http_consumer"),
#     route('websocket.connect', ws_add),
#     route('websocket.receive', ws_message),
#     route('websocket.disconnect', ws_disconnect),
# ]

from channels.routing import route
from chat.consumers import ws_connect, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect, path=r"^/anonymous-chat/(?P<room_label>[a-zA-Z0-9_]+)/?$"),
    route("websocket.receive", ws_message, path=r"^/anonymous-chat/(?P<room_label>[a-zA-Z0-9_]+)/?$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/anonymous-chat/(?P<room_label>[a-zA-Z0-9_]+)/?$"),
]