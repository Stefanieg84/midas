#!/bin/bash
set -e
echo "Starting local dev environment..."
docker-compose up -d
source .midas-venv/bin/activate
dbt compile --profiles-dir ./dbt
echo "Local setup complete. Airflow DAGs should be ready."