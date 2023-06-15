from app. __init__ import app
from app.functions import login_required_http, get_notification
from app.db_metadata import ENGINE, User, Friendshiprequest, Friendship

from flask import redirect, render_template, session, request
from sqlalchemy import select, delete
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
		user = sess.get(User, session["user_id"])
		sess.flush()
		friendship1 = Friendship(user_id=session["user_id"], friend_id=friend.id, friend_room=friend.room_id)
		friendship2 = Friendship(user_id=friend.id , friend_id=session["user_id"], friend_room=user.room_id)
		sess.add(friendship1)
		sess.add(friendship2)
		sess.execute(delete(Friendshiprequest).where(Friendshiprequest.sender_id == friend.id).where(Friendshiprequest.receiver_id == session["user_id"]))
		sess.commit()
	return redirect("/")

@app.route("/friends", methods=["POST", "GET"])
@login_required_http
def friends():
	sess = Session(ENGINE)
	stmt = select(User, Friendship).join(Friendship, User.id == Friendship.friend_id).where(Friendship.user_id == session["user_id"])
	friends = sess.execute(stmt).all()
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
	subquery3 = select(Friendship.friend_id).where(Friendship.user_id == session["user_id"])
	subquery4 = select(Friendship.user_id).where(Friendship.friend_id == session["user_id"])
	result = sess.execute(select(User).where(User.id.not_in(subquery1)).where(User.id.not_in(subquery2)).where(User.id.not_in(subquery3)).where(User.id.not_in(subquery4)).where(User.id != session["user_id"]))
	return render_template("search.html", app_name=app.config["APP_NAME"], filename=session["filename"], friends=result.scalars(), user_id=["user_id"], notification=get_notification())