import pytest
from consumer.app.main import app
from starlette.testclient import TestClient


@pytest.fixture
def test_app():
    client = TestClient(app)
    yield client
