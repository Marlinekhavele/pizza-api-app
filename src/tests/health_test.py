import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


# The health check must respond with a 200.
# This allows ECS to register a successful deployment.
# See iac/terraform/app/variables.tf if you wish to change this endpoint
@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/health")
    assert 200 == response.status_code
    assert {"status": "I'm alive"} == response.json()


@pytest.mark.asyncio
async def test_health_check_trailingslash(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/health/")
    assert 200 == response.status_code
    assert {"status": "I'm alive"} == response.json()
