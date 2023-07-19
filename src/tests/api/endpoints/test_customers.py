from uuid import uuid4

import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_customer(client: AsyncClient):
    customer_data = {
        "id": str(uuid4()),
        "name": "Marline k",
        "phone": "1234567890",
        "email": "marline.k@test.com",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/customers/", json=customer_data)
    assert response.status_code == 200
    assert response.json() == customer_data
