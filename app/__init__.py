from flask import Flask
from flask_socketio import SocketIO
import flask_session

import os
import os.path

APP_NAME = "main"

app = Flask(__name__)

# Confiqs
app.secret_key = "1"
app.config["APP_NAME"] = APP_NAME
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

# add support for server side session
flask_session.Session(app)

# make flask manage the session
socketio = SocketIO(app, manage_session=False) 

from app.main import *
from app.authentication import *
from app.sockets import *