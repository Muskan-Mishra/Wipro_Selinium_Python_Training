import requests

def test_user_schema(base_url):
    response = requests.get(f"{base_url}/users/2")

    data = response.json()

    assert isinstance(data, dict)
    assert "data" in data

    user = data["data"]

    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)