from flask import Flask
from flask_cors import *

from typing import Final

from components.config import *

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
}

SECONDS_IN_DAY: Final = 86400
SECONDS_IN_WEEK: Final = SECONDS_IN_DAY * 7
SECONDS_IN_MONTH: Final = SECONDS_IN_DAY * 30
