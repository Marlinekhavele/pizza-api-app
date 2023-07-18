import pytest
from httpx import AsyncClient

from app.main import app

TEST_BASE_URL = "http://test"


@pytest.fixture
def client():
    return AsyncClient(app=app)
