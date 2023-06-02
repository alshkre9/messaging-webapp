from flask import session
from app.__init__ import socketio
from flask_socketio import join_room, emit
from app.functions import login_required_websocket


@socketio.on("connect")
@login_required_websocket
def message(null):
    emit("sender_id", session["user_id"])

@socketio.on("send_message")
def message(value, sender_id):
    socketio.emit("receive_message", (value, sender_id))