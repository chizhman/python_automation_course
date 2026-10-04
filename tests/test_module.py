import pytest
import requests


@pytest.fixture
def url(pytestconfig):
    return pytestconfig.getoption("--url")

@pytest.fixture
def status_code(pytestconfig):
    return pytestconfig.getoption("--status_code")

def test_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code