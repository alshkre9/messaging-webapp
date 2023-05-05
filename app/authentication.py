from app.__init__ import app
from flask import session, render_template, request

@app.route("/sign_out")
def sign_out():
    session.clear()
    return "logout"

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    session.permanent = False
    session["user_id"] = 1
    return render_template("sign_in.html", app_name="main", path="/sign-in", name="sign in")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html", app_name="main", path="/sign-up", name="sign up")