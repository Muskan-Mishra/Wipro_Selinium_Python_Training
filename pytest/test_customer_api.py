import pytest
import requests
import responses

BASE_URL = "https://api.bankapp.com/customers"


@pytest.fixture(scope="module")
def customer_payload():
    return {
        "name": "Muskan Mishra",
        "email": "muskan@test.com",
        "balance": 5000
    }


@pytest.fixture(scope="module")
@responses.activate
def created_customer(customer_payload):
    # Mock POST
    responses.add(
        responses.POST,
        BASE_URL,
        json={"id": 101, **customer_payload},
        status=201
    )

    response = requests.post(BASE_URL, json=customer_payload)

    assert response.status_code == 201
    assert "id" in response.json()

    return response.json()["id"]


@responses.activate
def test_get_customer(created_customer, customer_payload):
    responses.add(
        responses.GET,
        f"{BASE_URL}/{created_customer}",
        json={"id": created_customer, **customer_payload},
        status=200
    )

    response = requests.get(f"{BASE_URL}/{created_customer}")

    assert response.status_code == 200
    assert response.json()["email"] == customer_payload["email"]


@responses.activate
def test_update_customer(created_customer):
    updated_payload = {
        "name": "Muskan Mishra",
        "email": "updated@test.com",
        "balance": 5000
    }

    responses.add(
        responses.PUT,
        f"{BASE_URL}/{created_customer}",
        json={"id": created_customer, **updated_payload},
        status=200
    )

    response = requests.put(
        f"{BASE_URL}/{created_customer}",
        json=updated_payload
    )

    assert response.status_code == 200
    assert response.json()["email"] == "updated@test.com"


@responses.activate
def test_delete_customer(created_customer):
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/{created_customer}",
        status=204
    )

    responses.add(
        responses.GET,
        f"{BASE_URL}/{created_customer}",
        status=404
    )

    delete_response = requests.delete(f"{BASE_URL}/{created_customer}")
    assert delete_response.status_code == 204

    get_response = requests.get(f"{BASE_URL}/{created_customer}")
    assert get_response.status_code == 404