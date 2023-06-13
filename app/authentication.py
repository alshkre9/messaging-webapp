from app.__init__ import app
from app.functions import get_valid_filename, valid_username, valid_password, logout_requierd
from app.db_metadata import *

from flask import session, render_template, request, redirect, url_for
from sqlalchemy import select
from sqlalchemy.orm import Session

from werkzeug.security import generate_password_hash, check_password_hash
from os.path import join
from PIL import Image

@app.route("/sign-out")
def sign_out():
    session.clear()
    return redirect(url_for("sign_in"))

@app.route("/sign-in", methods=["GET", "POST"])
@logout_requierd
def sign_in():
    if "POST" == request.method:
        username = request.form.get("username")
        password = request.form.get("password")
        if valid_username(username) and valid_password(password):
            sess = Session(ENGINE)
            sess.expire_on_commit = False
            stmt = select(User).where(User.username == username)
            for user in sess.execute(stmt).scalars():
                if check_password_hash(user.hash, password):
                    session["user_id"] = user.id
                    session["username"] = user.username
                    session["filename"] = user.filename
                    sess.commit()
                    return(redirect("/"))
        else:
            return "invalid username or password".title()

    return render_template("sign_in.html", app_name=app.config["APP_NAME"], path="/sign-in", name="sign in")

@app.route("/sign-up", methods=["GET", "POST"])
@logout_requierd
def sign_up():

    if "POST" == request.method:
        password = request.form.get("password")
        username = request.form.get("username")
        if valid_username(username) and valid_password(password):
            with Session(ENGINE) as sess:
                for user in sess.execute(select(User).where(User.username == username)).scalars():
                    if check_password_hash(user.hash, password):
                        sess.close()
                        return "username and password already taken"
                user = User(username=username, hash=generate_password_hash(password))
                sess.add(user)
                sess.flush()

                if (f := request.files["file"]):
                    if (filename := get_valid_filename(f.filename, user.id)):
                        f = Image.open(f)
                        f.thumbnail(app.config["PROFILE_IMAGES_DIMENSIONS"])
                        f.save(join(app.config["PROFILE_IMAGES"], filename))
                        user.filename = filename
                sess.commit()
                return redirect(url_for("sign_in"))
        else:
            return "invalid username or password".title()

    return render_template("sign_up.html", app_name=app.config["APP_NAME"], path="/sign-up", name="sign up")