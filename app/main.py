from app.__init__ import app
from app.functions import login_required
from flask import redirect, session, url_for, render_template, request


@app.route("/")
def index():
	return redirect("/friends")

@app.route("/friends", methods=["POST", "GET"])
@login_required
def friends():
	return render_template("friends.html", app_name="main", path=f"{url_for('search')}")

@app.route("/groups", methods=["POST", "GET"])
@login_required
def groups():
	return render_template("groups.html", app_name="main", path=f"{url_for('search')}")

@app.route("/search")
@login_required
def search():
	return str(request.values["q"])