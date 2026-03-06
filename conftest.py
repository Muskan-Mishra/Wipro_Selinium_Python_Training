import pytest
import requests
import json
import os


def load_config():
    """Load configuration from JSON file"""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_path, "r") as file:
        config = json.load(file)

    env = config["environment"]
    return config[env]


@pytest.fixture(scope="session")
def config():
    """Provide full environment config"""
    return load_config()


@pytest.fixture(scope="session")
def base_url(config):
    """Read Base URL from JSON config"""
    return config["base_url"]


@pytest.fixture(scope="session")
def auth_token():
    """Session-level token (simulated for demo API)"""
    print("\n[Setup] Generating Auth Token Once Per Session")
    token = "dummy-token-123"
    yield token
    print("\n[Teardown] Session Finished")


@pytest.fixture()
def user(base_url):
    """Create user before test and clean after"""
    print("\n[Setup] Creating Test User")

    response = requests.post(
        f"{base_url}/users",
        json={"name": "Priya", "job": "QA"}
    )

    user_id = response.json().get("id", "mock-id")

    yield user_id

    print("\n[Teardown] Cleanup (mock API)")