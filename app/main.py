from app.__init__ import app
from app.functions import login_required
from flask import redirect, session, url_for, render_template, request

@app.route("/", methods=["POST", "GET"])
@login_required
def main_page():
	return render_template("main.html", app_name="main", path=f"{url_for('search')}")

@app.route("/search")
@login_required
def search():
	return str(request.values["q"])