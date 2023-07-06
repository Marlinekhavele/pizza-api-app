from fastapi.testclient import TestClient


def test_endpoint_meta(client: TestClient):
    response = client.get("/api/meta")
    assert 200 == response.status_code
    assert {"app_version": "0.1.1"} == response.json()
