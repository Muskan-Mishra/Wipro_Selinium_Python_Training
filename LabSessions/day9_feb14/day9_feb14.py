import sys
import pytest
import requests

#1.Write a test that is skipped because a feature is not implemented yet.
@pytest.mark.skip(reason="Feature not implemented yet")
def test_new_feature():
    assert True


#2.write a test that runs only on Linux and skips on Windows.
@pytest.mark.skipif(sys.platform.startswith("win"), reason="Runs only on Linux")
def test_linux_only():
    assert True



#3.Write a test that checks an API health endpoint. If status code is not 200 → skip the test dynamically.
import pytest
import requests

def test_api_health():
    url = "https://jsonplaceholder.typicode.com/posts"  # sample API
    response = requests.get(url)

    if response.status_code != 200:
        pytest.skip("API is down. Skipping test.")

    assert response.status_code == 200


#4.Mark a failing test as xfail with reason: "Bug #123".
@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 2 + 2 == 5

#5.You have 5 parameterized cases. 2 are known bugs. Mark only those 2 cases as xfail without marking entire test.
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),  # normal case
        pytest.param(4, 5, 20, marks=pytest.mark.xfail(reason="Bug in calculation logic")),
        (10, 2, 12),  # normal case
        pytest.param(6, 6, 100, marks=pytest.mark.xfail(reason="Bug #456")),
        (1, 1, 2)  # normal case
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected