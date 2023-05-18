from __init__ import app, socketio
from flask import session, render_template, request, redirect
from werkzeug.utils import secure_filename
from os.path import join
from flask_socketio import join_room

@app.route("/sign_out")
def sign_out():
    session.clear()
    return "logout"

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if "user_id" in session:
        return redirect("/")
    session.permanent = False
    session["user_id"] = 3
    return render_template("sign_in.html", app_name=app.config["APP_NAME"], path="/sign-in", name="sign in")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if "POST" == request.method:
        if "file" in request.files:
            f = request.files["file"]
            f.save(join(app.config["PROFILE_IMAGES"], secure_filename(f.filename)))
    return render_template("sign_up.html", app_name=app.config["APP_NAME"], path="/sign-up", name="sign up")