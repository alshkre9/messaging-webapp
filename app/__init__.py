from flask import Flask, session

PROFILE_IMAGES = "profile_images/"
APP_NAME = "main"

app = Flask(__name__)
# Confiqs
app.secret_key = "1"
app.config["PROFILE_IMAGES"] = PROFILE_IMAGES 
app.config["APP_NAME"] = APP_NAME

from app.main import *
from app.authentication import *
