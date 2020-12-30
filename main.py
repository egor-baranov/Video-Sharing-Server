from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from data.User import *
from data.Video import *
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
}

users = [UserFactory.new_user(
    username="admin",
    password="password",
    email="admin@admin.com",
    birth_date="31.12.2000",
    city="city",
    phone="89004445533"
)]

blocked_users = []

videos = [
    Video(title="Видео для отладки 1", length=2374),
    Video(title="Видео для отладки 2", length=24),
    Video(title="Видео для отладки 3", length=123)
]

comments = []


def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    return User()


def get_user_by_phone(phone: str):
    for user in users:
        if user.phone == phone:
            return user
    return User()


def get_video_by_id(video_id: int):
    for video in videos:
        if video.video_id == video_id:
            return video


def get_comment_by_id(comment_id: int):
    for comment in comments:
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
    phone_user = get_user_by_phone(request.args.get("phone"))
    email_user = get_user_by_email(request.args.get("email"))
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

    users.append(user)
    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/list")
@cross_origin()
def full_list():
    resp = make_response(jsonify({
        "users": [u.to_dict() for u in users],
        "videos": [v.to_dict() for v in videos]
    }))
    resp.headers = headers
    return resp


@app.route("/videoList")
@cross_origin()
def video_list():
    resp = make_response(jsonify({
        "videos": [v.to_dict() for v in videos]
    }))
    resp.headers = headers
    return resp


@app.route("/userList")
@cross_origin()
def user_list():
    resp = make_response(jsonify({
        "users": [u.to_dict() for u in users]
    }))
    resp.headers = headers
    return resp


@app.route("/commentList")
@cross_origin()
def comment_list():
    resp = make_response(jsonify({
        "comments": [c.to_dict() for c in comments]
    }))
    resp.headers = headers
    return resp


@app.route("/addVideo")
@cross_origin()
def add_video():
    video = Video()

    video.title = request.args.get("title")
    video.description = request.args.get("description")
    video.tags = request.args.get("tags")
    video.size = int(request.args.get("size"))
    video.length = int(request.args.get("length"))
    video.cloudinary_id = int(request.args.get("id"))

    videos.append(video)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


@app.route("/getVideos")
@cross_origin()
def get_videos():
    count = int(request.args.get("count"))
    ret_videos = []
    for i in range(count):
        ret_videos.append(random.choice(videos).to_dict())
    resp = make_response(jsonify({"videos": ret_videos}))
    resp.headers = headers
    return resp


@app.route("/exist")
@cross_origin()
def exist():
    phone = request.args.get("phone")
    email = request.args.get("email")

    resp = make_response(
        jsonify({"ok": get_user_by_email(email).is_not_fake() or get_user_by_phone(phone).is_not_fake()}))
    resp.headers = headers
    return resp


@app.route("/likeVideo")
@cross_origin()
def like_video():
    video_id = int(request.args.get("videoId"))

    for i in range(len(videos)):
        if videos[i].cloudinary_id == video_id:
            videos[i].likes += 1
            resp = make_response(jsonify({"ok": True, "likeCount": videos[i].likes}))
            resp.headers = headers
            return resp


@app.route("/unlikeVideo")
@cross_origin()
def unlike_video():
    video_id = int(request.args.get("videoId"))

    for i in range(len(videos)):
        if videos[i].cloudinary_id == video_id:
            videos[i].likes -= 1
            resp = make_response(jsonify({"ok": True, "likeCount": videos[i].likes}))
            resp.headers = headers
            return resp


# admin-panel functions
@app.route("/blockUser")
@cross_origin()
def block_user():
    phone_user = get_user_by_phone(request.args.get("phone"))
    email_user = get_user_by_email(request.args.get("email"))

    if phone_user.is_not_fake():
        users.remove(phone_user)
        blocked_users.append(phone_user)
        resp = make_response(jsonify({"ok": True, "blockedUsers": blocked_users}))

    elif email_user.is_not_fake():
        users.remove(email_user)
        blocked_users.append(email_user)
        resp = make_response(jsonify({"ok": True, "blockedUsers": blocked_users}))

    else:
        resp = make_response(jsonify({"ok": False}))

    resp.headers = headers
    return resp


@app.route("/resetPassword")
@cross_origin()
def reset_password():
    phone = request.args.get("phone")
    email = request.args.get("email")

    for i in range(len(users)):
        if users[i].email == email or users[i].phone == phone:
            users[i].password = ""
            resp = make_response(jsonify({"ok": True, "users": users}))
            resp.headers = headers
            return resp

    resp = make_response(jsonify({"ok": False, "users": users}))
    resp.headers = headers
    return resp


@app.route("/deleteComment")
@cross_origin()
def delete_comment():
    comment_id = int(request.args.get("id"))

    if all([c.comment_id != comment_id for c in comments]):
        resp = make_response(jsonify({"ok": False}))
        resp.headers = headers
        return resp

    comment = get_comment_by_id(comment_id)

    comments.remove(comment)
    comment.text = "-Комментарий был удален администрацией-"
    comments.append(comment)

    resp = make_response(jsonify())
    resp.headers = headers
    return resp


if __name__ == "__main__":
    # app.debug = True
    app.run()
