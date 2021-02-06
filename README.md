# serratus-summary-api

## Desired routes

- `/api/nucleotide/sra=SRR10144611`
- `/api/rdrp/family=Coronaviridae`

## Current routes

- `/api/nucleotide/sra=SRR10144611`
- `/api/nucleotide/family=Coronaviridae`
- `/api/nucleotide/family=Coronaviridae?page=5`
- `/api/nucleotide/family=Coronaviridae?page=5&scoreMin=90&scoreMax=100`
- `/api/nucleotide/genbank=EU769558.1`

## TODO

- filter by score/pctid
- results from all tables for `sra_id`
- caching
- publish EB instance
- update serratus.io
