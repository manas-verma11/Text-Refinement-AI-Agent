import os

os.environ["GROQ_API_KEY"] = "test_key"

from fastapi.testclient import TestClient
from src.api.main import api


client = TestClient(api)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "Text Refinement AI Agent API"


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert "allowed_tones" in data
    assert "allowed_purposes" in data
    assert "allowed_use_cases" in data