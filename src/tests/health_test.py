from fastapi.testclient import TestClient


# The health check must respond with a 200.
# This allows ECS to register a successful deployment.
# See iac/terraform/app/variables.tf if you wish to change this endpoint
def test_health_check(client: TestClient):
    response = client.get("/api/health", allow_redirects=False)
    assert 200 == response.status_code
    assert {"status": "I'm alive"} == response.json()


def test_health_check_trailingslash(client: TestClient):
    response = client.get("api/health/", allow_redirects=False)
    assert 200 == response.status_code
    assert {"status": "I'm alive"} == response.json()
