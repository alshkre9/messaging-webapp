from app.__init__ import socketio
from app.functions import login_required_websocket
from app.db_metadata import ENGINE, Message

from flask import session
from flask_socketio import join_room, emit, leave_room
from sqlalchemy import select
from sqlalchemy.orm import Session


@socketio.on("connect")
@login_required_websocket
def connect(null):
    emit("user_id", session["user_id"])

@socketio.on("join")
@login_required_websocket
def on_join(room_id):
    try:
        if session["room_id"]:
            leave_room(session["room_id"])
    except KeyError:
        ...
    
    session["room_id"] = room_id
    join_room(room_id)
    with Session(ENGINE) as sess:
        for m in sess.execute(select(Message).where(Message.room_id == session["room_id"])).scalars():
            socketio.emit("receive_message", (m.value, m.user_id), to=session["room_id"])

@socketio.on("send_message")
def message(value, sender_id, room_id):
    with Session(ENGINE) as sess:
        m = Message(user_id=sender_id, room_id=room_id, value=value)
        sess.add(m)
        sess.commit()
    socketio.emit("receive_message", (value, sender_id), to=room_id)