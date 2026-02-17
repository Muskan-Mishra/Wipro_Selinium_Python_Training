import pytest
import requests
import responses

BASE_URL = "https://api.healthcareapp.com/v1"
TOKEN = "your_token_here"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


@pytest.fixture(scope="module")
def patient_id():
    return 101


@pytest.fixture(scope="module")
def doctor_id():
    return 201


@pytest.fixture(scope="module")
def appointment_id():
    return 301


@responses.activate
def test_full_appointment_flow(patient_id, doctor_id, appointment_id):

    responses.add(
        responses.POST,
        f"{BASE_URL}/patients",
        json={"patientId": patient_id},
        status=201
    )

    response = requests.post(
        f"{BASE_URL}/patients",
        json={
            "name": "Muskan Mishra",
            "age": 24,
            "gender": "Female",
            "contact": "9876543210"
        },
        headers=HEADERS
    )

    assert response.status_code == 201
    assert response.json()["patientId"] == patient_id

    responses.add(
        responses.POST,
        f"{BASE_URL}/doctors",
        json={"doctorId": doctor_id},
        status=201
    )

    response = requests.post(
        f"{BASE_URL}/doctors",
        json={
            "name": "Dr. Sharma",
            "specialization": "Cardiologist",
            "experience": 10
        },
        headers=HEADERS
    )

    assert response.status_code == 201
    assert response.json()["doctorId"] == doctor_id

    responses.add(
        responses.POST,
        f"{BASE_URL}/appointments",
        json={"appointmentId": appointment_id},
        status=201
    )

    response = requests.post(
        f"{BASE_URL}/appointments",
        json={
            "patientId": patient_id,
            "doctorId": doctor_id,
            "appointmentDate": "2026-02-20",
            "slot": "10:00 AM"
        },
        headers=HEADERS
    )

    assert response.status_code == 201
    assert response.json()["appointmentId"] == appointment_id

    responses.add(
        responses.PUT,
        f"{BASE_URL}/appointments/{appointment_id}",
        json={
            "appointmentId": appointment_id,
            "appointmentDate": "2026-02-22",
            "slot": "12:00 PM"
        },
        status=200
    )

    response = requests.put(
        f"{BASE_URL}/appointments/{appointment_id}",
        json={
            "appointmentDate": "2026-02-22",
            "slot": "12:00 PM"
        },
        headers=HEADERS
    )

    assert response.status_code == 200
    assert response.json()["appointmentDate"] == "2026-02-22"

    responses.add(
        responses.DELETE,
        f"{BASE_URL}/appointments/{appointment_id}",
        status=204
    )

    response = requests.delete(
        f"{BASE_URL}/appointments/{appointment_id}",
        headers=HEADERS
    )

    assert response.status_code == 204