import re

from flask import Flask
from flask_cors import *

from components.config import *
from lib.smsc_api import *
from phonenumbers import is_valid_number, parse

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_AS_ASCII"] = False

smsc = SMSC()


def is_phone_valid(phone_number: str) -> bool:
    return is_valid_number(parse(phone_number))


def is_email_valid(email: str) -> bool:
    pattern = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
    return pattern.match(email) is not None
