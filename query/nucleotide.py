from model.nucleotide import nsra, nfamily, nsequence
from . import apply_filters

per_page = 20

# sra

def get_families(sra):
    query = nfamily.query.filter(nfamily.sra_id == sra)
    return query.all()

def get_sequences(sra):
    query = nsequence.query.filter(nsequence.sra_id == sra)
    return query.all()

# family

def get_family_pagination(family, page, **kwargs):
    query = nfamily.query.filter(nfamily.family_name == family)
    query = apply_filters(query, nfamily, **kwargs)
    return query.paginate(page, per_page)
