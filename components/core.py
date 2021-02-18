from flask import Flask
from flask_cors import *

from components.config import *
from lib.smsc_api import *

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_AS_ASCII"] = False

smsc = SMSC()
