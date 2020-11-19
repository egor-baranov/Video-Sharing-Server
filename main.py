from flask import Flask, jsonify, request
from User import *
from Video import *

app = Flask(__name__)

newUser = User()
newUser.username = "admin"
newUser.password = "password"
newUser.email = "admin@admin.com"
newUser.birth_date = "31.12.2000"
newUser.city = "city"
newUser.phone = "89004445533"

users = [newUser]


videos = []


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
def main_page():
    return jsonify("Main Page")


@app.route("/login")
def login():
    phone_user = get_user_by_phone(request.args.get("phone"))
    email_user = get_user_by_email(request.args.get("email"))
    password = request.args.get("password")

    if phone_user.is_not_fake() and phone_user.password == password:
        return {"ok": True, "user": phone_user.to_dict()}

    if email_user.is_not_fake() and email_user.password == password:
        return {"ok": True, "user": email_user.to_dict()}

    return {"ok": False, "user": User().to_dict()}


@app.route("/register")
def register():
    user = User()

    user.username = request.args.get("username")
    user.phone = request.args.get("phone")
    user.password = request.args.get("password")
    user.email = request.args.get("email")
    user.city = request.args.get("city")
    user.birth_date = request.args.get("birthDate")

    users.append(user)
    return jsonify({"ok": True})


@app.route("/list")
def list_of_users():
    return jsonify({"users": [u.to_dict() for u in users],
                    "videos": [v.to_dict() for v in videos]})


@app.route("/addVideo")
def add_video():
    video = Video()

    video.title = request.args.get("title")
    video.description = request.args.get("description")
    video.tags = request.args.get("tags")
    video.size = int(request.args.get("size"))
    video.length = int(request.args.get("length"))

    videos.append(video)
    return jsonify({"ok": True})


@app.route("/getVideos")
def get_videos():
    count = int(request.args.get("count"))


@app.route("/exist")
def exist():
    phone = request.args.get("phone")
    email = request.args.get("email")
    return jsonify({"ok": get_user_by_email(email).is_not_fake() or get_user_by_phone(phone).is_not_fake()})


if __name__ == "__main__":
    # app.debug = True
    app.run()
