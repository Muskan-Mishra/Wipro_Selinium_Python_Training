import requests

def test_get_users(base_url, auth_token):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200


def test_get_single_user(base_url, auth_token):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200