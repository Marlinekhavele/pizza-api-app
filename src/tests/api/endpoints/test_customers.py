import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_customers(client: AsyncClient):
    customer_data = {
        "name": "khavele Mmbono",
        "phone": "1234567890",
        "email": "mbono.k@test.com",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/customers/", json=customer_data)
    assert response.status_code == 200
    customer_data["id"] = response.json()["id"]
    assert response.json() == customer_data


@pytest.mark.asyncio
async def test_get_customers(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/customers/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_customer_id(client: AsyncClient):
    # ensure customer exists before getting
    customer_obj = {
        "name": "khavele Mmbono",
        "phone": "1234567890",
        "email": "mbono.k@test.com",
    }
    await client.post(f"{TEST_BASE_URL}/api/customers/", json=customer_obj)
    get_response = await client.get(f"{TEST_BASE_URL}/api/customers/")
    assert get_response.status_code == 200


@pytest.mark.asyncio
async def test_update_customer_id(client: AsyncClient):
    customer_data = {
        "name": "khavele Mmbono",
        "phone": "1234567890",
        "email": "mbono.k@test.com",
    }
    response = await client.post(f"{TEST_BASE_URL}/api/customers/", json=customer_data)
    customer_id = response.json()["id"]
    response = await client.put(
        f"{TEST_BASE_URL}/api/customers/{customer_id}",
        json={
            **customer_data,
            "name": "marline",
            "email": "trisha.k@gmail.com",
            "phone": "+49123456",
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "marline"
    assert response.json()["email"] == "trisha.k@gmail.com"
    assert response.json()["phone"] == "+49123456"
