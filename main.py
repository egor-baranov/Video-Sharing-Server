from flask import make_response, jsonify, request

from components.core import *

from components.core import headers
from components.database.dbworker import DatabaseWorker
from components.managers.UserManager import UserManager
from components.managers.VideoManager import VideoManager
from data.User import *
from data.Video import *
import random

def get_comment_by_id(comment_id: int):
    for comment in DatabaseWorker.Comments:
        if comment.comment_id == comment_id:
            return comment


@app.route("/")
@cross_origin()
def main_page():
    resp = make_response(jsonify("Main Page"))
    resp.headers = headers
    return resp


@app.route("/login")
@cross_origin()
def login():
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    password = request.args.get("password")

    if phone_user.is_not_fake() and phone_user.password == password:
        resp = make_response(jsonify({
            "ok": True,
            "user": phone_user.to_dict()
        }))

    elif email_user.is_not_fake() and email_user.password == password:
        resp = make_response(jsonify({
            "ok": True,
            "user": email_user.to_dict()
        }))

    else:
        resp = make_response(jsonify({"ok": False, "user": User().to_dict()}))

    resp.headers = headers
    return resp


@app.route("/register")
@cross_origin()
def register():
    user = UserFactory.new_user(
        username=request.args.get("username"),
        phone=request.args.get("phone"),
        password=request.args.get("password"),
        email=request.args.get("email"),
        city=request.args.get("city"),
        birth_date=request.args.get("birthDate")
    )

    UserManager.add_user(user)
    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


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
    resp = make_response(jsonify({
        "users": [u.to_dict() for u in DatabaseWorker.read_users()]
    }))
    resp.headers = headers
    return resp


@app.route("/commentList")
@cross_origin()
def comment_list():
    resp = make_response(jsonify({
        "comments": [c.to_dict() for c in DatabaseWorker.Comments]
    }))
    resp.headers = headers
    return resp


@app.route("/addVideo")
@cross_origin()
def add_video():
    video = Video()

    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user

    video.title = request.args.get("title")
    video.description = request.args.get("description")
    video.tags = request.args.get("tags")
    video.size = int(request.args.get("size"))
    video.length = int(request.args.get("length"))
    video.video_id = int(request.args.get("videoId"))

    user.uploaded_videos.append(video.video_id)

    UserManager.update_user_data(user)
    VideoManager.add_video(video)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/getVideos")
@cross_origin()
def get_videos():
    count = int(request.args.get("count"))
    ret_videos = []
    for i in range(count):
        ret_videos.append(random.choice(DatabaseWorker.read_videos()).to_dict())
    resp = make_response(jsonify({"videos": ret_videos}))
    resp.headers = headers
    return resp


@app.route("/getFavourite")
@cross_origin()
def get_favourite():
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user
    resp = make_response(jsonify({"ok": True, "result": user.liked_videos}))
    resp.headers = headers
    return resp


@app.route("/exist")
@cross_origin()
def exist():
    phone = request.args.get("phone")
    email = request.args.get("email")

    resp = make_response(
        jsonify({"ok": UserManager.get_user_by_email(email).is_not_fake() or UserManager.get_user_by_phone(
            phone).is_not_fake()}))
    resp.headers = headers
    return resp


@app.route("/likeVideo")
@cross_origin()
def like_video():
    video_id = int(request.args.get("videoId"))
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user

    videos = DatabaseWorker.read_videos()

    for i in range(len(videos)):
        if videos[i].video_id == video_id:
            if video_id in user.liked_videos:
                user.liked_videos.remove(video_id)
                videos[i].likes -= 1
            else:
                user.liked_videos.append(video_id)
                videos[i].likes += 1

            resp = make_response(
                jsonify({"ok": True, "likeCount": videos[i].likes,
                         "isLiked": video_id in user.liked_videos}))
            DatabaseWorker.write_videos(videos)
            UserManager.update_user_data(user)
            resp.headers = headers
            return resp
    resp = make_response(jsonify({"ok": False}))
    DatabaseWorker.write_videos(videos)
    UserManager.update_user_data(user)
    resp.headers = headers
    return resp


@app.route("/videoLikeCount")
@cross_origin()
def video_like_count():
    video_id = int(request.args.get("videoId"))
    email_user = UserManager.get_user_by_email(request.args.get("email"))
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))

    if email_user.is_fake() and phone_user.is_fake():
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    user = email_user if email_user.is_not_fake() else phone_user

    resp = make_response(
        jsonify({"ok": True, "likeCount": VideoManager.get_video_by_id(video_id).likes, "isLiked": video_id in user.liked_videos}))
    resp.headers = headers
    return resp


# admin-panel functions
@app.route("/blockUser")
@cross_origin()
def block_user():
    phone_user = UserManager.get_user_by_phone(request.args.get("phone"))
    email_user = UserManager.get_user_by_email(request.args.get("email"))

    if phone_user.is_not_fake():
        UserManager.block_user(phone_user)
        resp = make_response(jsonify({"ok": True, "blockedUsers": DatabaseWorker.read_blocked_users()}))

    elif email_user.is_not_fake():
        UserManager.block_user(email_user)
        resp = make_response(jsonify({"ok": True, "blockedUsers": DatabaseWorker.read_blocked_users()}))

    else:
        resp = make_response(jsonify({"ok": False}))

    resp.headers = headers
    return resp


@app.route("/resetPassword")
@cross_origin()
def reset_password():
    phone = request.args.get("phone")
    email = request.args.get("email")

    users = DatabaseWorker.read_users()

    for i in range(len(users)):
        if users[i].email == email or users[i].phone == phone:
            users[i].password = ""
            resp = make_response(jsonify({"ok": True, "users": users}))
            DatabaseWorker.write_users(users)
            resp.headers = headers
            return resp

    resp = make_response(jsonify({"ok": False, "users": users}))
    DatabaseWorker.write_users(users)
    resp.headers = headers
    return resp


@app.route("/deleteComment")
@cross_origin()
def delete_comment():
    comment_id = int(request.args.get("id"))

    if all([c.comment_id != comment_id for c in DatabaseWorker.Comments]):
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    comment = get_comment_by_id(comment_id)

    DatabaseWorker.Comments.remove(comment)
    comment.text = "-Комментарий был удален администрацией-"
    DatabaseWorker.Comments.append(comment)

    resp = make_response(jsonify())
    resp.headers = headers
    return resp


if __name__ == "__main__":
    # app.debug = True
    app.run()
