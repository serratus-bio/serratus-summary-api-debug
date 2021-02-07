from flask import Flask, jsonify
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    from model import db
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()
application = app  # for AWS EB
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

import route.nucleotide

@app.errorhandler(Exception)
def server_error(e):
    return jsonify(error=repr(e)), 500
