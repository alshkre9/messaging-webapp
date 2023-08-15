from app. __init__ import app
from app.helper import login_required_http
from app.db_metadata import Message

from flask import redirect, render_template, session

@app.route("/")
def index():
	return redirect("/chats")

@app.route("/chats", methods=["GET"])
@login_required_http
def friends():
	messages = Message.get()
	return render_template("main.chats.html", app_name=app.config["APP_NAME"], messages=messages)

@app.route("/hello", methods=["GET"])
@login_required_http
def search():
	return "hello"