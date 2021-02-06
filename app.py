from flask import Flask, jsonify, request
from flask_cors import CORS
from query.nucleotide import get_families, get_sequences, get_family_pagination


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    from model import db
    db.init_app(app)
    return app

app = create_app()
application = app  # for AWS EB
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/nucleotide/sra=<sra>')
def get_sra(sra):
    families = get_families(sra)
    sequences = get_sequences(sra)
    return jsonify(families=families, sequences=sequences)


@app.route('/api/nucleotide/family=<family>')
def get_family(family):
    page = int(request.args.get('page', 1))
    scoreMin = request.args.get('scoreMin', None)
    scoreMax = request.args.get('scoreMax', None)
    if scoreMin:
        scoreMin = int(scoreMin)
    if scoreMax:
        scoreMax = int(scoreMax)
    pagination = get_family_pagination(family, page,
        scoreMin=scoreMin,
        scoreMax=scoreMax)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
