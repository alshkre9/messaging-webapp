from app.__init__ import app
from app.functions import get_valid_filename, valid_username, valid_password
from app.db_metadata import *

from flask import session, render_template, request, redirect
from sqlalchemy.orm import Session

from werkzeug.security import generate_password_hash
from os.path import join
from PIL import Image

@app.route("/sign_out")
def sign_out():
    session.clear()
    return "logout"

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if "user_id" in session:
        return redirect("/")
    return render_template("sign_in.html", app_name=app.config["APP_NAME"], path="/sign-in", name="sign in")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if "POST" == request.method:
        password = request.form.get("password")
        username = request.form.get("username").title()
        if valid_username(username) and valid_password(password):
            with Session(ENGINE) as sess:
                user = User(username=username, hash=generate_password_hash(password))
                sess.add(user)
                sess.flush()
    
                if (f := request.files["file"]):
                    if (filename := get_valid_filename(f.filename, user.id)):
                        f = Image.open(f).resize(app.config["PROFILE_IMAGES_DIMENSIONS"])
                        f.save(join(app.config["PROFILE_IMAGES"], filename))
                        user.filename = filename
                sess.commit()
        else:
            return "non valid username and password".title()

    return render_template("sign_up.html", app_name=app.config["APP_NAME"], path="/sign-up", name="sign up")