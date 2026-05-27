from fastapi.testclient import TestClient
from app.main import app
import json
import pytest
from datetime import datetime, timedelta


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    responseData = json.loads(response.content)
    assert responseData["status"] == "ok"
    assert responseData["version"] == "1.0.0"
    assert responseData["environment"] == "dev"
    actualTimestamp = datetime.fromisoformat(responseData["timestamp"])
    expectedTimestamp = datetime.now()
    assert abs(expectedTimestamp - actualTimestamp) <= timedelta(seconds=1)