#!/bin/bash
set -e
echo "Starting Airbyte…"
(cd airbyte && docker compose up -d)

echo "Starting Midas local dev environment..."
docker-compose up -d
source .midas-venv/bin/activate
dbt compile --profiles-dir ./dbt
echo "Local setup complete. Airflow DAGs should be ready."
