from channels.routing import route
from chat.consumers import ws_message, ws_add, ws_disconnect

channel_routing = [
    # route("http.request", "chat.consumers.http_consumer"),
    route('websocket.connect', ws_add),
    route('websocket.receive', ws_message),
    route('websocket.disconnect', ws_disconnect),
]
