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

videos = [
    Video(title="Видео для отладки 1", length=2374),
    Video(title="Видео для отладки 2", length=24),
    Video(title="Видео для отладки 3", length=123)
]


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
def list_of_users():
    resp = make_response(jsonify({
        "users": [u.to_dict() for u in users],
        "videos": [v.to_dict() for v in videos]
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
    video_list = []
    for i in range(count):
        video_list.append(random.choice(videos).to_dict())
    resp = make_response(jsonify({"videos": video_list}))
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


if __name__ == "__main__":
    # app.debug = True
    app.run()
