from flask_sqlalchemy_caching import FromCache
from model.nucleotide import nsra, nfamily, nsequence
from . import apply_filters
from application import cache


per_page = 20

# sra

def get_sra_properties(sra):
    query = nsra.query.filter(nsra.sra_id == sra)
    return query.one()

def get_sra_families(sra):
    query = nfamily.query.filter(nfamily.sra_id == sra)
    return query.all()

def get_sra_sequences(sra):
    query = nsequence.query.filter(nsequence.sra_id == sra)
    return query.all()

# family

def get_family_pagination(family, page=1, **kwargs):
    page = int(page)
    query = (nfamily.query
        .filter(nfamily.family_name == family)
        .order_by(nfamily.score.desc())
        .options(FromCache(cache)))
    query = apply_filters(query, nfamily, **kwargs)
    return query.paginate(page, per_page)

# genbank

def get_genbank_pagination(genbank, page=1, **kwargs):
    page = int(page)
    query = (nsequence.query
        .filter(nsequence.genbank_id == genbank)
        .order_by(nsequence.score.desc())
        .options(FromCache(cache)))
    query = apply_filters(query, nsequence, **kwargs)
    return query.paginate(page, per_page)
