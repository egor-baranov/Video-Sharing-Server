from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.managers.UserManager import UserManager

user_editing_blueprint = Blueprint(
    "edit", __name__, template_folder="templates", static_folder="static"
)


@app.route("/editUserName")
@cross_origin()
def edit_user_name():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user
    user.username = request.args.get("username")
    UserManager.update_user_data(user)


@app.route("/editUserBirthDate")
@cross_origin()
def edit_user_birth_date():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user
    user.birth_date = request.args.get("birthDate")
    UserManager.update_user_data(user)


@app.route("/editUserCity")
@cross_origin()
def edit_user_city():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user
    user.city = request.args.get("city")
    UserManager.update_user_data(user)
