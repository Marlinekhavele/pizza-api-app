# import pytest
# from httpx import AsyncClient
# from uuid import uuid4


# from conftest import TEST_BASE_URL


# @pytest.mark.asyncio
# async def test_create_product(client: AsyncClient):
#     product_data = {
#         "id": str(uuid4()),
#         "title": "Samosa",
#         "description": "This samosa's are the best in town and vegeterian",
#         "price": "10.00",
#     }

#     response = await client.post(f"{TEST_BASE_URL}/api/products/", json=product_data)
#     assert response.status_code == 200
#     assert response.json() == product_data
