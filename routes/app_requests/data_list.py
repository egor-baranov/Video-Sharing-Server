from flask import make_response, jsonify, request
from flask import Blueprint

from components.database.dbworker import DatabaseWorker
from components.core import *
from dto.User import UserFactory

data_list_blueprint = Blueprint("list", __name__, template_folder="templates", static_folder="static")


@app.route("/list")
@cross_origin()
def full_list():
    resp = make_response(jsonify({
        "users": [u.to_dict() for u in DatabaseWorker.read_users()],
        "videos": [v.to_dict() for v in DatabaseWorker.read_videos()]
    }))
    resp.headers = headers
    return resp


@app.route("/videoList")
@cross_origin()
def video_list():
    resp = make_response(jsonify({
        "videos": [v.to_dict() for v in DatabaseWorker.read_videos()]
    }))
    resp.headers = headers
    return resp


@app.route("/userList")
@cross_origin()
def user_list():
    count = int(request.args.get("count") if request.args.get("count") is not None else 100)

    sort_type = request.args.get("sortType") if request.args.get("sortType") is not None else "username"

    if sort_type not in UserFactory.new_fake_user().to_dict().keys():
        sort_type = "username"

    resp_list = [u.to_dict() for u in DatabaseWorker.read_users()]

    if len(resp_list) > count:
        resp_list = resp_list[:count]

    resp_list.sort(key=lambda x: x[sort_type])

    resp = make_response(jsonify({
        "users": resp_list
    }))
    resp.headers = headers
    return resp


@app.route("/commentList")
@cross_origin()
def comment_list():
    resp = make_response(jsonify({
        "comments": [c.to_dict() for c in DatabaseWorker.read_comments()]
    }))
    resp.headers = headers
    return resp
