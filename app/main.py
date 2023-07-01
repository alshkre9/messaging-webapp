from app. __init__ import app
from app.functions import login_required_http, get_notification
from app.db_metadata import ENGINE, User, Friendshiprequest, Friendship

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
		with Session(ENGINE) as sess:
			friend = sess.get(User, request.form.get("user_id"))
			friendship1 = Friendship(user_id=session["user_id"], friend_id=friend.id)
			friendship2 = Friendship(user_id=friend.id , friend_id=session["user_id"])
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
	friends = sess.execute(stmt)
	return render_template("friends.html", app_name=app.config["APP_NAME"], filename=session["filename"], friends=friends.all(), user_id=session["user_id"], notification=get_notification(), session=sess)

# @app.route("/groups", methods=["POST", "GET"])
# @login_required_http
# def groups():
# 	return redirect("/")

@app.route("/search", methods=["POST", "GET"])
@login_required_http
def search():
	sess = Session(ENGINE)
	if "POST" == request.method:
		if user_id := request.form.get("add"):
			result1 = sess.execute(select(Friendshiprequest).where(Friendshiprequest.sender_id == session["user_id"]).where(Friendshiprequest.receiver_id == user_id)).one_or_none()
			result2 = sess.execute(select(Friendshiprequest).where(Friendshiprequest.receiver_id == session["user_id"]).where(Friendshiprequest.sender_id == user_id)).one_or_none()
			result3 = sess.execute(select(Friendship).where(Friendship.user_id == session["user_id"]).where(Friendship.friend_id == user_id)).one_or_none()
			if not result1 and not result2 and not result3:
				sess.add(Friendshiprequest(sender_id=session["user_id"], receiver_id=user_id))
		else:
			user_id = request.form.get("remove")
			sess.delete(sess.execute(select(Friendship).where(Friendship.user_id == session["user_id"]).where(Friendship.friend_id == user_id)).scalar())
			sess.delete(sess.execute(select(Friendship).where(Friendship.user_id == user_id).where(Friendship.friend_id == session["user_id"])).scalar())
		sess.commit()
	users = sess.execute(select(User).where(User.id != session["user_id"]))
	friends = sess.execute(select(Friendship.user_id).where(Friendship.friend_id == session["user_id"]))
	# store it in a list because scalarresult object is an iterator
	friends = [x for x in friends.scalars()]
	return render_template("search.html", app_name=app.config["APP_NAME"], filename=session["filename"], users=users.scalars(), friends=friends, notification=get_notification(), session=sess)