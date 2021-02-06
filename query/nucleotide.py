from model.nucleotide import nsra, nfamily, nsequence

tables = {
    'nsra': nsra,
    'nfamily': nfamily,
    'nsequence': nsequence
}

per_page = 20

# sra

def get_families(sra):
    query = nfamily.query.filter(nfamily.sra_id == sra)
    return query.all()

def get_sequences(sra):
    query = nsequence.query.filter(nsequence.sra_id == sra)
    return query.all()

# family

def get_family_pagination(family, page, scoreMin=None, scoreMax=None):
    query = nfamily.query.filter(nfamily.family_name == family)
    if scoreMin:
        query = query.filter(nfamily.score >= scoreMin)
    if scoreMax:
        query = query.filter(nfamily.score <= scoreMax)
    return query.paginate(page, per_page)
