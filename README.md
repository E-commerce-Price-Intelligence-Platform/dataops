# DataOps — E-commerce Price Intelligence Platform

## Role
Responsable DataOps : infrastructure, automatisation, monitoring et qualite des donnees.

## Architecture DataOps

Web Scraping -> NiFi (Streaming) + Airflow (Batch) -> Bigtable -> dbt -> Statistics
                          |
                    DataOps Layer
                    - Docker + Kubernetes
                    - CI/CD (GitHub Actions)
                    - Monitoring (Prometheus + Grafana)
                    - Data Quality (Great Expectations)
                    - Infrastructure (Terraform)

## Structure du repo

dataops/
├── docker-compose.yml
├── terraform/
│   └── main.tf
├── kubernetes/
│   └── deployment.yml
├── great_expectations/
│   └── data_quality_checks.py
├── monitoring/
│   └── prometheus.yml
└── .github/
    └── workflows/
        └── ci.yml

## Lancer le projet localement

docker compose up -d

## Services

| Service    | Port | Description              |
|------------|------|--------------------------|
| Prometheus | 9090 | Collecte des metriques   |
| Grafana    | 3000 | Dashboard de monitoring  |

## Data Quality

python great_expectations/data_quality_checks.py

Verifie : prix positifs, champs non vides, plateformes valides, pas de doublons.

## CI/CD

GitHub Actions lance automatiquement les tests a chaque push sur main.

## Infrastructure Cloud Terraform

terraform init
terraform plan
terraform apply

Deploie : Google Cloud Bigtable + Google Kubernetes Engine GKE.