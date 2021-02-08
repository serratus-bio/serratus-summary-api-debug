from flask import jsonify, request
from flask import current_app as app
from query.nucleotide import (
    get_sra_properties,
    get_sra_families,
    get_sra_sequences,
    get_family_pagination,
    get_genbank_pagination
)
from werkzeug.contrib.cache import SimpleCache


cache_timeout = 0  # no timeout
sra_cache = SimpleCache()

@app.route('/api/nucleotide/sra=<sra>')
def get_sra(sra):
    return get_sra_cache(sra)


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


def get_sra_cache(sra):
    response = sra_cache.get(sra)
    if response:
        return response
    properties = get_sra_properties(sra)
    families = get_sra_families(sra)
    sequences = get_sra_sequences(sra)
    response = jsonify(properties=properties, families=families, sequences=sequences)
    sra_cache.set(sra, response, timeout=cache_timeout)
    return response
