from flask import make_response, jsonify

from components.core import *

from routes.admin_panel.admin_requests import admin_requests_blueprint
from routes.admin_panel.user_editing import user_editing_blueprint

from routes.app_requests.regular_requests import regular_requests_blueprint
from routes.app_requests.data_list import data_list_blueprint

app.register_blueprint(admin_requests_blueprint)
app.register_blueprint(user_editing_blueprint)

app.register_blueprint(regular_requests_blueprint)
app.register_blueprint(data_list_blueprint)


@app.route("/")
@cross_origin()
def main_page():
    resp = make_response(jsonify("Main Page"))
    resp.headers = headers
    return resp


if __name__ == "__main__":
    app.run()
