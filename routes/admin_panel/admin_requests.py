import time

from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.database.DatabaseWorker import DatabaseWorker
from components.managers.CommentManager import CommentManager
from components.managers.UserManager import UserManager

admin_requests_blueprint = Blueprint(
    "admin", __name__, template_folder="templates", static_folder="static"
)


@app.route("/blockUser")
@cross_origin()
def block_user():
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))
    email_user = UserManager.get_user_by_email(request.args.get("email"))

    if phone_user.is_not_fake():
        UserManager.block_user(phone_user)
        resp = make_response(
            jsonify(
                {
                    "ok": True,
                    "blockedUsers": [
                        u.to_dict() for u in DatabaseWorker.read_blocked_users()
                    ],
                }
            )
        )

    elif email_user.is_not_fake():
        UserManager.block_user(email_user)
        resp = make_response(
            jsonify(
                {
                    "ok": True,
                    "blockedUsers": [
                        u.to_dict() for u in DatabaseWorker.read_blocked_users()
                    ],
                }
            )
        )

    else:
        resp = make_response(jsonify({"ok": False}))

    resp.headers = headers
    return resp


@app.route("/removeUser")
@cross_origin()
def remove_user():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user
    UserManager.remove_user(user)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/getStats")
@cross_origin()
def get_stats():
    resp = make_response(
        jsonify(
            {
                "ok": True,
                "videosUploadedCount": {
                    "forLastDay": sum(
                        [
                            (time.time() - v.upload_time) <= SECONDS_IN_DAY
                            for v in DatabaseWorker.read_videos()
                        ]
                    ),
                    "forLastWeek": sum(
                        [
                            (time.time() - v.upload_time) <= SECONDS_IN_WEEK
                            for v in DatabaseWorker.read_videos()
                        ]
                    ),
                    "forLastMonth": sum(
                        [
                            (time.time() - v.upload_time) <= SECONDS_IN_MONTH
                            for v in DatabaseWorker.read_videos()
                        ]
                    ),
                    "overall": len(DatabaseWorker.read_videos())
                },
                "usersRegisteredCount": {
                    "forLastDay": sum(
                        [
                            (time.time() - u.register_time) <= SECONDS_IN_DAY
                            for u in DatabaseWorker.read_users()
                        ]
                    ),
                    "forLastWeek": sum(
                        [
                            (time.time() - u.register_time) <= SECONDS_IN_WEEK
                            for u in DatabaseWorker.read_users()
                        ]
                    ),
                    "forLastMonth": sum(
                        [
                            (time.time() - u.register_time) <= SECONDS_IN_MONTH
                            for u in DatabaseWorker.read_users()
                        ]
                    ),
                    "overall": len(DatabaseWorker.read_users())
                },
                "commentsLeftCount": {
                    "forLastDay": sum(
                        [
                            (time.time() - c.creation_time) <= SECONDS_IN_DAY
                            for c in DatabaseWorker.read_comments()
                        ]
                    ),
                    "forLastWeek": sum(
                        [
                            (time.time() - c.creation_time) <= SECONDS_IN_WEEK
                            for c in DatabaseWorker.read_comments()
                        ]
                    ),
                    "forLastMonth": sum(
                        [
                            (time.time() - c.creation_time) <= SECONDS_IN_MONTH
                            for c in DatabaseWorker.read_comments()
                        ]
                    ),
                    "overall": len(DatabaseWorker.read_comments())
                },
                "usedDiscSpace": {
                    "dataServer": str(float("{:.2f}".format(DatabaseWorker.get_used_disc_space() / 10 ** 6))) + " MB",
                    "mediaServer": "? MB"
                }
            }
        )
    )
    resp.headers = headers
    return resp


@app.route("/restoreUser")
@cross_origin()
def restore_user():
    pass

@app.route("/resetPassword")
@cross_origin()
def reset_password():
    phone = request.args.get("phone")
    email = request.args.get("email")

    users = DatabaseWorker.read_users()

    for i in range(len(users)):
        if users[i].email == email or users[i].phone == phone:
            users[i].password = ""
            resp = make_response(
                jsonify(
                    {
                        "ok": True,
                        "users": [u.to_dict() for u in DatabaseWorker.read_users()],
                    }
                )
            )
            DatabaseWorker.write_users(users)
            resp.headers = headers
            return resp

    resp = make_response(
        jsonify(
            {"ok": False, "users": [u.to_dict() for u in DatabaseWorker.read_users()]}
        )
    )
    DatabaseWorker.write_users(users)
    resp.headers = headers
    return resp


@app.route("/deleteComment")
@cross_origin()
def delete_comment():
    comment_id = int(request.args.get("id"))

    if not CommentManager.does_comment_exist(comment_id):
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    CommentManager.delete_comment(comment_id)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/getRole")
@cross_origin()
def get_role():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user

    resp = make_response(jsonify({"ok": True, "role": user.role}))
    resp.headers = headers
    return resp


@app.route("/setRole")
@cross_origin()
def set_role():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user
    user.role = request.args.get("role")
    UserManager.update_user_data(user)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp
