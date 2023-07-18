# import pytest
# from httpx import AsyncClient
# from uuid import uuid4

# # from app.deps import get_db_session
# # from app.models import Customer
# from conftest import TEST_BASE_URL


# @pytest.mark.asyncio
# async def test_create_order(client: AsyncClient):
#     order_data = {
#         "id": str(uuid4()),
#         "customer_id": str(uuid4()),
#         "status": "Processing",
#     }

#     response = await client.post(f"{TEST_BASE_URL}/api/orders/", json=order_data)
#     assert response.status_code == 200
#     assert response.json() == order_data

