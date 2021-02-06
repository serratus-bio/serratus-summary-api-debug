from flask import Flask, jsonify, request
from flask_cors import CORS
from query.nucleotide import (
    get_sra_properties,
    get_sra_families,
    get_sra_sequences,
    get_family_pagination,
    get_genbank_pagination
)


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
    properties = get_sra_properties(sra)
    families = get_sra_families(sra)
    sequences = get_sra_sequences(sra)
    return jsonify(properties=properties, families=families, sequences=sequences)


@app.route('/api/nucleotide/family=<family>')
def get_family(family):
    page = int(request.args.get('page', 1))
    pagination = get_family_pagination(family, **request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)


@app.route('/api/nucleotide/genbank=<genbank>')
def get_genbank(genbank):
    page = int(request.args.get('page', 1))
    pagination = get_genbank_pagination(genbank, **request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
