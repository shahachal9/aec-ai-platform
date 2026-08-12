from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "AEC AI Platform"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_organization():
    response = client.post(
        "/api/organizations",
        json={"name": "Demo AEC Company"},
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Demo AEC Company"
