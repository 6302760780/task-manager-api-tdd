import pytest
from app.store import reset_store


@pytest.fixture(autouse=True)
def clear_store():
    reset_store()