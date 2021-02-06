def apply_filters(query, model, scoreMin=None, scoreMax=None):
    if scoreMin:
        query = query.filter(model.score >= int(scoreMin))
    if scoreMax:
        query = query.filter(model.score <= int(scoreMax))
    return query
