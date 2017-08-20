import json
from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs


# Connected to websocket.connect
def ws_connect(message, room_name):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat-%s" % room_name).add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message, room_name):
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "text": message["text"],
        }),
    })


# Connected to websocket.disconnect
def ws_disconnect(message, room_name):
    Group("chat-%s" % room_name).discard(message.reply_channel)
