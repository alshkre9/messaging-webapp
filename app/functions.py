from app.__init__ import app

from flask import redirect, session, url_for
from flask_socketio import disconnect

from werkzeug.utils import secure_filename
from functools import wraps
from re import compile


def login_required_http(f):
    @wraps(f)
    def func(*args, **kwargs):
        if not "user_id" in session:
            return redirect(url_for("sign_in"))
        else:
            return f(*args, **kwargs)
    return func

def login_required_websocket(f):
    @wraps(f)
    def func(*args, **kwargs):
        if not "user_id" in session:
            disconnect()
        else:
            return f(*args, **kwargs)
    return func

def logout_requierd(f):
    @wraps(f)
    def func(*args, **kwargs):
        if "user_id" in session:
            return redirect("/")
        else:
            return f(*args, **kwargs)
    return func


def get_valid_filename(filename, user_id):
    filename = secure_filename(filename)
    if valid_filename_extension(filename):
        return str(user_id) + "." + filename.rsplit(".", 1)[1]
    return None

def valid_filename_extension(filename: str) -> bool:
    return filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

def valid_username(username: str) -> bool:
    engine = compile("^[0-9-A-Za-z]|_{8,28}$")
    return (true := engine.search(username))

def valid_password(password: str) -> bool:
    engine = compile("^.{8,28}$")
    return (true := engine.search(password))
