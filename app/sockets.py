from flask import session
from __init__ import socketio
from flask_socketio import join_room, emit
from functions import login_required_websocket


@socketio.on("connect")
@login_required_websocket
def message(null):
    emit("user_id", session["user_id"])

@socketio.on("send_message")
def message(value, user_id):
    socketio.emit("receive_message", (value, user_id))