from __init__ import app
from functions import login_required
from flask import redirect, session, url_for, render_template, request


@app.route("/")
def index():
	return redirect("/friends")

@app.route("/friends", methods=["POST", "GET"])
@login_required
def friends():
	return render_template("friends.html", app_name=app.config["APP_NAME"])

@app.route("/groups", methods=["POST", "GET"])
@login_required
def groups():
	return render_template("groups.html", app_name=app.config["APP_NAME"])

@app.route("/search")
@login_required
def search():
	return render_template("search.html", app_name=app.config["APP_NAME"])