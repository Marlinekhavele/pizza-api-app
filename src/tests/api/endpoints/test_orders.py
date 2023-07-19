from uuid import uuid4

import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_order(client: AsyncClient):

    customer_response = await client.post(f"{TEST_BASE_URL}/api/customers/",json={
        "id": str(uuid4()),
        "name": "marline",
        "email": "trisha.k@gmail.com",
        "phone": "+49123456"
    }   
    )
    order_data = {
        "id": str(uuid4()),
        "customer_id": customer_response.json()['id'],
        "status": "Delivered",
    }
    response = await client.post(f"{TEST_BASE_URL}/api/orders/", json=order_data)
    assert customer_response.status_code == 200
    assert response.json() == order_data

@pytest.mark.asyncio
async def test_get_orders(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/orders/")
    assert response.status_code == 200
