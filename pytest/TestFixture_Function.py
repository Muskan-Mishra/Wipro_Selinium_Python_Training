import pytest

@pytest.mark.usefixtures("openbrowser", "closebrowser")
def test_login():
    print("enter username")
    print("enter password")
    print("click login")

@pytest.mark.usefixtures("openbrowser", "closebrowser")
def test_logout():
    print("user logged out")