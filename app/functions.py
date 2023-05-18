from functools import wraps
from flask import redirect, session, url_for
from flask_socketio import disconnect


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
