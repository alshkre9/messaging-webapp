from flask import Flask, session
from flask_socketio import SocketIO, emit, send
from flask_session import Session

PROFILE_IMAGES = "profile_images/"
APP_NAME = "main"

app = Flask(__name__)

# Confiqs
app.secret_key = "1"
app.config["PROFILE_IMAGES"] = PROFILE_IMAGES 
app.config["APP_NAME"] = APP_NAME
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# add support for server side session
Session(app)

# make flask manage the session
socketio = SocketIO(app, manage_session=False) 

from app.main import *
from app.authentication import *
from app.sockets import *