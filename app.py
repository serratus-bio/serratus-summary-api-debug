from flask import Flask, jsonify, request
from flask_cors import CORS
from query import get_pagination


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    from model import db
    db.init_app(app)
    return app

app = create_app()
application = app  # for AWS EB
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/<table>/<column>=<value>')
def get(table, column, value):
    page = int(request.args.get('page', 1))
    pagination = get_pagination(table, column, value, page)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
