import pytest
from httpx import AsyncClient

# from app.deps import get_db_session
# from app.models import Customer
from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_customer(client: AsyncClient):
    customer_data = {
        "id": "ae7554e6-549b-4975-87b0-2e7b98c450e0",
        "name": "Marline k",
        "phone": "1234567890",
        "email": "marline.k@test.com",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/customers/", json=customer_data)
    assert response.status_code == 200
    assert response.json() == customer_data
