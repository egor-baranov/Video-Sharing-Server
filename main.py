from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def main_page():
    return jsonify("Main Page")


if __name__ == '__main__':
    # app.debug = True
    app.run()
