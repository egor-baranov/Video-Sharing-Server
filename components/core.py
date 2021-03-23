import re

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


def is_phone_valid(phone_number):
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    return pattern.match(phone_number) is not None


def is_email_valid(email):
    pattern = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
    return pattern.match(email) is not None
