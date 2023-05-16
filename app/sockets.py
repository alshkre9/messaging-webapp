from flask import session
from __init__ import socketio
from flask_socketio import join_room

@socketio.on("send_message")
def message(value, room):
    socketio.emit("receive_message", value, to=room)