from __init__ import socketio
from helper import login_required_websocket
from models import Message

from flask import session
from flask_socketio import join_room, emit, leave_room
from sqlalchemy import select, or_
from sqlalchemy.orm import Session


@socketio.on("connect")
@login_required_websocket
def connect(null):
    emit("user_room", session["user_id"])
    for message in Message.get():
        emit("receive_message", message.value, session["user_id"])

@socketio.on("send_message")
def message(value):
    Message.create(from_=session["user_id"], value=value)
    socketio.emit("receive_message", (value, session["user_id"]))