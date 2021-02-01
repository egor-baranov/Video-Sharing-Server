from flask import Flask
from flask_cors import *

from typing import Final

from components.config import *

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
