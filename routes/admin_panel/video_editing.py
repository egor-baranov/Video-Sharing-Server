from flask import make_response, jsonify, request
from flask import Blueprint

from components.core import *
from components.managers.VideoManager import VideoManager

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


@app.route("/editVideoTegs")
@cross_origin()
def edit_video_tegs():
    pass
