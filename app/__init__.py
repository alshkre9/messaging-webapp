from flask import Flask
from flask_socketio import SocketIO
import flask_session

APP_NAME = "main"
PROFILE_IMAGES = "profile_images/"
PROFILE_IMAGES_DIMENSIONS = (100, 100)
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

app = Flask(__name__)

# Confiqs
app.secret_key = "1"
app.config["APP_NAME"] = APP_NAME
app.config["PROFILE_IMAGES"] = PROFILE_IMAGES 
app.config["PROFILE_IMAGES_DIMENSIONS"] = PROFILE_IMAGES_DIMENSIONS
app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

# add support for server side session
flask_session.Session(app)

# make flask manage the session
socketio = SocketIO(app, manage_session=False) 

from app.main import *
from app.authentication import *
from app.sockets import *