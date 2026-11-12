from fastapi.testclient import TestClient

from app import app, search_catalog

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_scholarship_query_returns_official_source():
    response = client.get("/search", params={"q": "student scholarship"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["count"] >= 1
    assert payload["results"][0]["id"] == "national-scholarship-portal"
    assert payload["results"][0]["source"]["url"] == "https://scholarships.gov.in/Students"


def test_unsupported_query_abstains():
    response = client.get("/search", params={"q": "intergalactic submarine repair"})
    assert response.status_code == 200
    assert response.json()["results"] == []
    assert "No matching source" in response.json()["message"]


def test_empty_query_returns_helpful_message():
    response = client.get("/search", params={"q": "   "})
    assert response.status_code == 200
    assert response.json()["count"] == 0
    assert response.json()["message"] == "Enter a search query."


def test_search_is_case_insensitive():
    lower = search_catalog("student scholarship")
    upper = search_catalog("STUDENT SCHOLARSHIP")
    assert [item["id"] for item in lower] == [item["id"] for item in upper]
