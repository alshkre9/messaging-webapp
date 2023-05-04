from functools import wraps
from flask import redirect, session, url_for


def login_required(f):
    @wraps(f)
    def func(*args, **kwargs):
        if not "user_id" in session:
            return redirect(url_for("sign_in"))
        else:
            return f(*args, **kwargs)
    return func
