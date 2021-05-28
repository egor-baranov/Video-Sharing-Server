from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.managers.VideoManager import VideoManager
from components.managers.VideoManager import Video

video_editing_blueprint = Blueprint(
    "edit", __name__, template_folder="templates", static_folder="static"
)


@app.route("/editVideoTitle")
@cross_origin()
def edit_video_title():
    pass


@app.route("/editVideoDescription")
@cross_origin()
def edit_video_description():
    pass


@app.route("/editVideoTags")
@cross_origin()
def edit_video_tags():
    pass


@app.route("/updatePromotionalVideo")
@cross_origin()
def update_promotional_video():
    video_id: int = int(request.args.get("videoId"))
    video: Video = VideoManager.get_video_by_id(video_id)

    video.max_show_count = int(request.args.get("maxShowCount"))
    video.display_option = request.args.get("displayOption")
    video.title = request.args.get("title")

    VideoManager.update_video_data(video)

    resp = make_response(jsonify({"ok": True, "video": video.to_dict()}))
    resp.headers = headers
    return resp


@app.route("/deletePromotionalVideo")
@cross_origin()
def delete_promotional_video():
    video_id: int = int(request.args.get("videoId"))
    VideoManager.delete_video(video_id)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp


