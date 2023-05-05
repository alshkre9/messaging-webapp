from app.__init__ import app
from app.functions import login_required
from flask import redirect, session, url_for, render_template

@app.route("/")
@login_required
def main_page():
	return render_template("main_page.html")