import pytest
import requests

@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_status_codes(status_code):
    response = requests.get(f"https://httpbin.org/status/{status_code}")
    assert response.status_code == status_code