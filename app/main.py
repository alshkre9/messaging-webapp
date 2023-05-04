from app.__init__ import app
from app.functions import login_required
from flask import redirect, session, url_for, render_template

@app.route("/")
@login_required
def index():
	return render_template("base.html")