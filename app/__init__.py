from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "1"
SESSION_TYPE = "filesystem"
SESSION_PERMANENT = False
app.config.from_object(__name__)
Session(app)

from app.main import *
from app.authentication import *
