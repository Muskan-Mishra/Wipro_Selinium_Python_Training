import pytest

pytestmark = pytest.mark.usefixtures("openbrowser_module", "closebrowser_module")

def test_login():
    print("enter username")
    print("enter password")
    print("click login")

def test_logout():
    print("user logged out")