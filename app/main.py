from app. __init__ import app
from app.functions import login_required_http, get_notification
from app.db_metadata import ENGINE, User, Group, Friendshiprequest, Friendship, Room, Room_type

from flask import redirect, render_template, session, request
from sqlalchemy import select, delete, or_
from sqlalchemy.orm import Session


@app.route("/")
def index():
	return redirect("/friends")

@app.route("/accept", methods=["POST", "GET"])
@login_required_http
def accept():
	if "POST" == request.method:
		sess = Session(ENGINE)
		friend = sess.get(User, request.form.get("user_id"))
		room = Room(model="Friendship")
		sess.add(room)
		sess.flush()
		friendship = Friendship(user_id1=friend.id, user_id2=session["user_id"], room_id=room.id)
		sess.add(friendship)
		sess.execute(delete(Friendshiprequest).where(Friendshiprequest.sender_id == friend.id).where(Friendshiprequest.receiver_id == session["user_id"]))
		sess.commit()
	return redirect("/")

@app.route("/friends", methods=["POST", "GET"])
@login_required_http
def friends():
	sess = Session(ENGINE)
	stmt1 = select(User, Friendship.room_id).where(User.id == Friendship.user_id1).where(Friendship.user_id2 == session["user_id"])
	stmt2 = select(User, Friendship.room_id).where(User.id == Friendship.user_id2).where(Friendship.user_id1 == session["user_id"])
	friends = []
	friends += sess.execute(stmt1).all()
	friends += sess.execute(stmt2).all()
	return render_template("friends.html", app_name=app.config["APP_NAME"], filename=session["filename"], friends=friends, user_id=session["user_id"], notification=get_notification())

@app.route("/groups", methods=["POST", "GET"])
@login_required_http
def groups():
	return redirect("/")

@app.route("/search", methods=["POST", "GET"])
@login_required_http
def search():
	sess = Session(ENGINE)
	if "POST" == request.method:
		user_id = request.form.get("id")
		result = sess.execute(select(User, Friendshiprequest).join(Friendshiprequest, User.id == Friendshiprequest.sender_id).where(Friendshiprequest.receiver_id == session["user_id"])).one_or_none()
		if not result:
			sess.add(Friendshiprequest(sender_id=session["user_id"], receiver_id=user_id))
			sess.commit()
	subquery1 = select(Friendshiprequest.sender_id).where(Friendshiprequest.receiver_id == session["user_id"])
	subquery2 = select(Friendshiprequest.receiver_id).where(Friendshiprequest.sender_id == session["user_id"])
	subquery3 = select(Friendship.user_id1).where(Friendship.user_id2 == session["user_id"])
	subquery4 = select(Friendship.user_id2).where(Friendship.user_id1 == session["user_id"])
	result = sess.execute(select(User).where(User.id.not_in(subquery1)).where(User.id.not_in(subquery2)).where(User.id.not_in(subquery3)).where(User.id.not_in(subquery4)).where(User.id != session["user_id"]))
	return render_template("search.html", app_name=app.config["APP_NAME"], filename=session["filename"], friends=result.scalars(), user_id=["user_id"], notification=get_notification())