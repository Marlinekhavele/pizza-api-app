from uuid import uuid4

import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_product(client: AsyncClient):
    product_data = {
        "id": str(uuid4()),
        "title": "Magaritta",
        "description": "Best magarita",
        "price": "4.50",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/products/", json=product_data)
    assert response.status_code == 200
    assert response.json() == product_data


@pytest.mark.asyncio
async def test_get_products(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/products")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_product_id(client: AsyncClient):
    # ensure product exists before getting
    product_obj = {
        "id": str(uuid4()),
        "title": "Bolognese",
        "description": "Best Bolognese",
        "price": "4.50",
    }
    await client.post(f"{TEST_BASE_URL}/api/products", json=product_obj)
    get_response = await client.get(f"{TEST_BASE_URL}/api/products")
    assert get_response.status_code == 200


@pytest.mark.asyncio
async def test_update_product_id(client: AsyncClient):
    product_data = {
        "id": str(uuid4()),
        "title": "Bolognese",
        "description": "Best Bolognese",
        "price": "4.50",
    }
    await client.post(f"{TEST_BASE_URL}/api/products/", json=product_data)
    product_id = product_data["id"]
    response = await client.put(
        f"{TEST_BASE_URL}/api/products/{product_id}",
        json={
            "id": str(uuid4()),
            "title": "salami pizza",
            "description": "Best pizza",
            "price": "10.50",
        },
    )
    assert response.status_code == 200
    assert response.json()["title"] == "salami pizza"
    assert response.json()["description"] == "Best pizza"
    assert response.json()["price"] == "10.50"
