from  __init__ import app
from helper import login_required_http
from models import Message

from flask import redirect, render_template, session

@app.route("/")
def index():
	return redirect("/chats")

@app.route("/chats", methods=["GET"])
@login_required_http
def friends():
	return render_template("main.chats.html", app_name=app.config["APP_NAME"], messages=Message.get())

@app.route("/profile", methods=["GET"])
@login_required_http
def profile():
	return "hello"