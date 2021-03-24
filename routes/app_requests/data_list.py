from flask import make_response, jsonify, request
from flask import Blueprint

from components.database.DatabaseWorker import DatabaseWorker
from components.core import *
from components.managers.UserManager import UserManager
from dto.User import UserFactory

data_list_blueprint = Blueprint(
    "list", __name__, template_folder="templates", static_folder="static"
)


@app.route("/list")
@cross_origin()
def full_list():
    resp = make_response(
        jsonify(
            {
                "users": [u.to_dict() for u in DatabaseWorker.read_users()],
                "videos": [v.to_dict() for v in DatabaseWorker.read_videos()],
            }
        )
    )
    resp.headers = headers
    return resp


@app.route("/videoList")
@cross_origin()
def video_list():
    limit = int(
        request.args.get("limit") if request.args.get("limit") is not None else 100
    )
    page = int(
        request.args.get("page") if request.args.get("page") is not None else 1
    )
    sort_type = (
        request.args.get("sortType")
        if request.args.get("sortType") is not None
        else "title"
    )

    resp_list = [v.to_dict() for v in DatabaseWorker.read_videos()]

    for i in range(len(resp_list)):
        d = resp_list[i]
        d["authorUsername"] = UserManager.get_video_owner(d["videoId"]).username
        d["authorPhone"] = UserManager.get_video_owner(d["videoId"]).phone
        d["authorEmail"] = UserManager.get_video_owner(d["videoId"]).email
        resp_list[i] = d

    resp_list.sort(key=lambda x: x[sort_type])

    try:
        resp_list = resp_list[limit * (page - 1):limit * page]
        resp = make_response(
            jsonify({"videos": resp_list})
        )
        resp.headers = headers
        return resp
    except():
        resp = make_response(
            jsonify({"videos": resp_list, "totalCount": len(resp_list)})
        )
        resp.headers = headers
        return resp


@app.route("/userList")
@cross_origin()
def user_list():
    limit = int(
        request.args.get("limit") if request.args.get("limit") is not None else 100
    )
    page = int(
        request.args.get("page") if request.args.get("page") is not None else 1
    )

    sort_type = (
        request.args.get("sortType")
        if request.args.get("sortType") is not None
        else "username"
    )

    if sort_type not in UserFactory.new_fake_user().to_dict().keys():
        sort_type = "username"

    resp_list = []
    for u in DatabaseWorker.read_users():
        if u.is_not_fake():
            resp_list.append(u.to_dict())

    resp_list.sort(key=lambda x: x[sort_type])

    try:
        resp_list = resp_list[limit * (page - 1):limit * page]
        resp = make_response(jsonify({"users": resp_list, "totalCount": len(resp_list)}))
        resp.headers = headers
        return resp
    except():
        resp = make_response(jsonify({"users": resp_list, "totalCount": len(resp_list)}))
        resp.headers = headers
        return resp


@app.route("/blockedUserList")
@cross_origin()
def blocked_user_list():
    resp = make_response(
        jsonify({"users": [u.to_dict() for u in DatabaseWorker.read_blocked_users()]})
    )
    resp.headers = headers
    return resp


@app.route("/commentList")
@cross_origin()
def comment_list():
    resp = make_response(
        jsonify({"comments": [c.to_dict() for c in DatabaseWorker.read_comments()]})
    )
    resp.headers = headers
    return resp
