from app.__init__ import socketio
from app.functions import login_required_websocket
from app.db_metadata import ENGINE, Message

from flask import session
from flask_socketio import join_room, emit, leave_room
from sqlalchemy import select, or_
from sqlalchemy.orm import Session


@socketio.on("connect")
@login_required_websocket
def connect(null):
    join_room(session["room_id"])
    emit("user_room", session["room_id"])

@socketio.on("join")
@login_required_websocket
def on_join(room_id):

    try:
        if session["joined_room"]:
            leave_room(session["joined_room"])
    except KeyError:
        ...
    session["joined_room"] = int(room_id)
    join_room(room_id)

    with Session(ENGINE) as sess:
        for m in sess.execute(select(Message).where(or_(Message.from_room == session["room_id"], Message.from_room == room_id)).where(or_(Message.to_room == room_id, Message.to_room == session["room_id"])).order_by(Message.date)).scalars():
            emit("receive_message", (m.value, m.from_room), to=session["room_id"])

@socketio.on("send_message")
def message(value, to_room):
    with Session(ENGINE) as sess:
        m = Message(from_room=session["room_id"], to_room=to_room, value=value)
        sess.add(m)
        sess.commit()
    socketio.emit("receive_message", (value, to_room), to=int(to_room))
    socketio.emit("receive_message", (value, session["room_id"]), to=session["room_id"])