import requests
import os

AIRBYTE_URL = os.getenv("AIRBYTE_API_BASE_URL")

def trigger_sync(connection_id: str):
    r = requests.post(
        f"{AIRBYTE_URL}/api/v1/connections/sync",
        json={"connectionId": connection_id},
        timeout=30
    )
    r.raise_for_status()
    return r.json()

def trigger_health(connection_id: str):
    r = requests.post(
        f"{AIRBYTE_URL}/api/v1/health",
        json={"connectionId": connection_id},
        timeout=30
    )
    r.raise_for_status()
    return r.json()