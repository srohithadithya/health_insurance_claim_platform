import os
import sys

os.environ["DEMO_MODE"] = "true"

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_claim_invalid_insurance():
    response = client.post("/claim", json={
        "insurance_id": "",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "condition": "fever"
    })
    assert response.status_code == 422

def test_claim_valid_structure():
    response = client.post("/claim", json={
        "insurance_id": "ABHA123456",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "condition": "fever"
    })
    assert response.status_code == 200
    data = response.json()
    assert "insurance_valid" in data
    assert "facilities" in data
    assert "doctors" in data
    assert "alternatives" in data
    assert data["provider_name"] == "ABHA Health"
    assert "ai_suggestion" not in data

def test_claim_employee_insurance():
    response = client.post("/claim", json={
        "insurance_id": "EMP88219",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "condition": "fracture",
        "insurance_type": "employee",
        "company_name": "Google",
        "employee_id": "G-1002"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["insurance_valid"] == True
    assert data["provider_name"] == "Google Corporate Health (Employee)"
