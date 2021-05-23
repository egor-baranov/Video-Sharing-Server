import time

from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.database.DatabaseWorker import DatabaseWorker
from components.managers.CommentManager import CommentManager
from components.managers.UserManager import UserManager
from components.managers.VideoManager import VideoManager
from dto.Video import Video

admin_requests_blueprint = Blueprint(
    "admin", __name__, template_folder="templates", static_folder="static"
)


@app.route("/blockUser")
@cross_origin()
def block_user():
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_not_fake():
        UserManager.block_user(user)
        resp = make_response(
            jsonify({
                "ok": True,
                "blockedUsers": [
                    u.to_dict() for u in DatabaseWorker.read_blocked_users()
                ],
            })
        )
    else:
        resp = make_response(jsonify({"ok": False}))

    resp.headers = headers
    return resp


@app.route("/removeUser")
@cross_origin()
def remove_user():
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

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
                    "mediaServer": str(
                        float("{:.2f}".format(sum([v.size for v in DatabaseWorker.read_videos()]) / 10 ** 6))
                    ) + " MB",
                    "overall":
                        str(float("{:.2f}".format(
                            (sum([v.size for v in DatabaseWorker.read_videos()]) +
                             DatabaseWorker.get_used_disc_space()) / 10 ** 6))) + " MB",
                },
                "userLocations": [u.coordinates for u in DatabaseWorker.read_users()]
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
    user = UserManager.get_user_by_id(int(request.args.get("userId")))
    if user.is_not_fake():
        user.password = ""
        UserManager.update_user_data(user)

    resp = make_response(
        jsonify({"ok": user.is_not_fake(), "users": [u.to_dict() for u in DatabaseWorker.read_users()]})
    )
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
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    resp = make_response(jsonify({"ok": True, "role": user.role}))
    resp.headers = headers
    return resp


@app.route("/setRole")
@cross_origin()
def set_role():
    user = UserManager.get_user_by_id(int(request.args.get("userId")))

    if user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user.role = request.args.get("role")
    UserManager.update_user_data(user)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/addPromotionalVideo")
@cross_origin()
def add_promotional_video():
    video = Video()
    video.title = request.args.get("title")
    video.size = int(request.args.get("size"))
    video.length = int(request.args.get("length"))
    video.video_id = int(request.args.get("videoId"))
    video.max_show_count = int(request.args.get("maxShowCount"))
    video.display_option = request.args.get("displayOption")

    video.is_promotional = True

    VideoManager.add_video(video)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/getParameters")
@cross_origin()
def get_parameters():
    resp = make_response(
        jsonify({
            "ok": True,
            "promotionalVideoFrequency":
                app.config.get("promotionalVideoFrequency") if "promotionalVideoFrequency" in app.config.keys() else -1
        })
    )
    resp.headers = headers
    return resp


@app.route("/setParameters")
@cross_origin()
def set_parameters():
    app.config["promotionalVideoFrequency"] = int(request.args.get("promotionalVideoFrequency"))
    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp
