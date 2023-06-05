from app. __init__ import app
from app.functions import login_required_http
from app.db_metadata import ENGINE, User, Group

from flask import redirect, render_template, session, request
from sqlalchemy import select
from sqlalchemy.orm import Session


@app.route("/")
def index():
	return redirect("/friends")

@app.route("/friends", methods=["POST", "GET"])
@login_required_http
def friends():
	return render_template("friends.html", app_name=app.config["APP_NAME"], filename=session["filename"])

@app.route("/groups", methods=["POST", "GET"])
@login_required_http
def groups():
	return render_template("groups.html", app_name=app.config["APP_NAME"], filename=session["filename"])

@app.route("/search", methods=["POST", "GET"])
@login_required_http
def search():
	sess = Session(ENGINE)
	result = sess.execute(select(User).where(User.id != session["user_id"]))
	return render_template("search.html", app_name=app.config["APP_NAME"], filename=session["filename"], friends=result.scalars())