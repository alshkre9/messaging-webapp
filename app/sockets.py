from app.__init__ import socketio
from app.helper import login_required_websocket, send
from app.models import Message

from flask import session
from flask_socketio import join_room, emit, leave_room
from sqlalchemy import select, or_
from sqlalchemy.orm import Session


@socketio.on("connect")
@login_required_websocket
def connect(null):
    emit("user_room", session["user_id"])
    result = Message.get()
    for message in result["messages"]:
        send(message.value)
    result["session"].close()

@socketio.on("send_message")
def message(value):
    Message.create(from_=session["user_id"], value=value)
    send(value)