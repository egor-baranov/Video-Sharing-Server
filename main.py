from flask import make_response, jsonify

from components.core import *


@app.route("/")
@cross_origin()
def main_page():
    resp = make_response(jsonify("Main Page"))
    resp.headers = headers
    return resp


if __name__ == "__main__":
    # app.debug = True
    app.run()
