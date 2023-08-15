from app.__init__ import socketio
from app.helper import login_required_websocket
from app.db_metadata import ENGINE, Message

from flask import session
from flask_socketio import join_room, emit, leave_room
from sqlalchemy import select, or_
from sqlalchemy.orm import Session


@socketio.on("connect")
@login_required_websocket
def connect(null):
    join_room(int(session["user_id"]))
    emit("user_room", session["user_id"])

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
        query = select(Message).where(or_(Message.from_ == session["user_id"], Message.from_ == room_id)).where(or_(Message.to == room_id, Message.to == session["user_id"])).order_by(Message.date)
        for m in sess.execute(query).scalars():
            emit("receive_message", (m.value, m.from_), to=int(session["user_id"]))

@socketio.on("send_message")
def message(value, to):
    Message.create(from_=session["user_id"], to=to, value=value)
    socketio.emit("receive_message", (value, session["user_id"]), to=int(to))
    socketio.emit("receive_message", (value, session["user_id"]), to=int(session["user_id"]))