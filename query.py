from model.nucleotide import nsra, nfamily, nsequence

tables = {
    'nsra': nsra,
    'nfamily': nfamily,
    'nsequence': nsequence
}

per_page = 20

def get_pagination(table, column, value, page):
    query = get_filtered_query(table, column, value)
    return query.paginate(page, per_page)


def get_filtered_query(table, column, value):
    table = tables[table]
    return table.query.filter(getattr(table, column) == value)
