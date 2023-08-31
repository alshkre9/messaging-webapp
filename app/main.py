from app. __init__ import app
from app.helper import login_required_http
from app.models import Message

from flask import redirect, render_template, session

@app.route("/")
def index():
	return redirect("/chats")

@app.route("/chats", methods=["GET"])
@login_required_http
def friends():
	return render_template("main.chats.html", app_name=app.config["APP_NAME"])

# @app.route("/profile", methods=["GET"])
# @login_required_http
# def profile():
# 	return "profile"

# @app.route("/settings", methods=["GET"])
# @login_required_http
# def settings():
# 	return "settings"