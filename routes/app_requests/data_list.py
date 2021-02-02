from flask import make_response, jsonify, request
from flask import Blueprint

from components.database.dbworker import DatabaseWorker
from components.core import *

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
    count = int(request.args.get("count"))

    resp_list = [u.to_dict() for u in DatabaseWorker.read_users()]

    if len(resp_list) > count:
        resp_list = resp_list[:count]

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
