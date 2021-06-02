from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.managers.UserManager import UserManager

user_editing_blueprint = Blueprint(
    "userEditing", __name__, template_folder="templates", static_folder="static"
)


@app.route("/editUserName")
@cross_origin()
def edit_user_name():
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user.username = request.args.get("username")
    UserManager.update_user_data(user)

    resp = make_response(jsonify({"ok": True, "userData": user.to_dict()}))
    resp.headers = headers
    return resp


@app.route("/editUserBirthDate")
@cross_origin()
def edit_user_birth_date():
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user.birth_date = request.args.get("birthDate")
    UserManager.update_user_data(user)

    resp = make_response(jsonify({"ok": True, "userData": user.to_dict()}))
    resp.headers = headers
    return resp


@app.route("/editUserCity")
@cross_origin()
def edit_user_city():
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user.city = request.args.get("city")
    UserManager.update_user_data(user)

    resp = make_response(jsonify({"ok": True, "userData": user.to_dict()}))
    resp.headers = headers
    return resp
