# serratus-summary-api

## Example routes

- [`/api/nucleotide/sra=ERR2756788`](https://api.serratus.io/api/nucleotide/sra=ERR2756788)
- [`/api/nucleotide/family=Coronaviridae`](https://api.serratus.io/api/nucleotide/family=Coronaviridae)
- [`/api/nucleotide/family=Coronaviridae?page=5`](https://api.serratus.io/api/nucleotide/family=Coronaviridae?page=5)
- [`/api/nucleotide/family=Coronaviridae?scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/api/nucleotide/family=Coronaviridae?scoreMin=90&scoreMax=100&page=5)
- [`/api/nucleotide/family=Coronaviridae?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/api/nucleotide/family=Coronaviridae?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
- [`/api/nucleotide/genbank=EU769558.1`](https://api.serratus.io/api/nucleotide/genbank=EU769558.1)
- [`/api/nucleotide/genbank=EU769558.1?page=5`](https://api.serratus.io/api/nucleotide/genbank=EU769558.1?page=5)
- [`/api/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/api/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&page=5)
- [`/api/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/api/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)

## SQL indexes for optimal querying

```sql
CREATE INDEX nfamily_sra_id_index ON nfamily (sra_id);
CREATE INDEX nsequence_sra_id_index ON nsequence (sra_id);
CREATE INDEX nsequence_genbank_id_index ON nsequence (genbank_id);
```

## AWS Setup

### Elastic Beanstalk

- Application name: **serratus-summary-api-flask**
- Environment
    - Web server environment
    - Name: **serratus-summary-api**
    - Platform: Python (3.7 running on 64bit Amazon Linux 2)
    - Sample app (will be overidden by CodePipeline deployment)

After creation:

- Add load balancer listener
    - Port: 443
    - Protocol: HTTPS
    - SSL certificate: `*.serratus.io`
- Processes
    - Health check path: `/api/nucleotide/sra=ERR2756788`

### CodePipeline

1. Settings
    - Pipeline name: **serratus-summary-api-flask**
    - New service role
2. Source stage
    - Source provider: GitHub (Version 1)
    - Select this repo/branch
    - Change detection: GitHub webhooks
3. Build stage: skip
4. Deploy stage
    - Provider: AWS Elastic Beanstalk
    - Region: us-east-1
    - Application/environment names from above

### IAM

- `aws-elasticbeanstalk-ec2-role`: Attach policy **AmazonRDSDataFullAccess**

### Route 53

- `A` record for `api.serratus.io` -> Elastic Beanstalk endpoint

## TODO

- caching
- `/api/protein/*`
- `/api/rdrp/*`
