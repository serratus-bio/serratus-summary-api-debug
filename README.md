# serratus-summary-api

## Desired routes

- `/api/nucleotide/sra=ERR2756788`
- `/api/rdrp/family=Coronaviridae`

## Current routes

- `/api/nucleotide/sra=ERR2756788`
- `/api/nucleotide/family=Coronaviridae`
- `/api/nucleotide/family=Coronaviridae?page=5`
- `/api/nucleotide/family=Coronaviridae?scoreMin=90&scoreMax=100&page=5`
- `/api/nucleotide/family=Coronaviridae?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`
- `/api/nucleotide/genbank=EU769558.1`
- `/api/nucleotide/genbank=EU769558.1?page=5`
- `/api/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&page=5`
- `/api/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`

## SQL indexes for optimal querying

```sql
CREATE INDEX nfamily_sra_id_index ON nfamily (sra_id);
CREATE INDEX nsequence_sra_id_index ON nsequence (sra_id);
CREATE INDEX nsequence_genbank_id_index ON nsequence (genbank_id);
```

## TODO

- caching
- publish EB instance
- update serratus.io
