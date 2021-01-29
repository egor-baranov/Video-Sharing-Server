from components.core import *
from flask import make_response, jsonify, request
from flask_cors import cross_origin


@app.route("/editUserName")
@cross_origin()
def edit_user_name():
    pass


@app.route("/editUserBirthDate")
@cross_origin()
def edit_user_birth_date():
    pass


@app.route("/editUserCity")
@cross_origin()
def edit_user_city():
    pass
