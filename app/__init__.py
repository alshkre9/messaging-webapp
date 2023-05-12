from flask import Flask, session

app = Flask(__name__)
app.secret_key = "1"

from app.main import *
from app.authentication import *
