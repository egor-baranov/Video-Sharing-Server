from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.managers.VideoManager import VideoManager
from components.managers.VideoManager import Video

video_editing_blueprint = Blueprint(
    "videoEditing", __name__, template_folder="templates", static_folder="static"
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

    if VideoManager.get_video_by_id(video_id) is None:
        resp = make_response(jsonify({"ok": False, "error": "Video with this id doesn't exist."}))
        resp.headers = headers
        return resp

    video: Video = VideoManager.get_video_by_id(video_id)

    if not video.is_promotional:
        if VideoManager.get_video_by_id(video_id) is None:
            resp = make_response(
                jsonify({"ok": False, "error": "Video with this id is not promotional."})
            )
            resp.headers = headers
            return resp

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

    if VideoManager.get_video_by_id(video_id) is None:
        resp = make_response(jsonify({"ok": False, "error": "Video with this id doesn't exist."}))
        resp.headers = headers
        return resp

    if not VideoManager.get_video_by_id(video_id).is_promotional:
        if VideoManager.get_video_by_id(video_id) is None:
            resp = make_response(
                jsonify({"ok": False, "error": "Video with this id is not promotional."})
            )
            resp.headers = headers
            return resp

    VideoManager.delete_video(video_id)

    resp = make_response(jsonify({"ok": True}))
    resp.headers = headers
    return resp
