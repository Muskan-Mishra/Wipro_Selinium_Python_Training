import pytest

@pytest.mark.usefixtures("openbrowser_class", "closebrowser_class")
class TestLogin:

    def test_login(self):
        print("enter username")
        print("enter password")
        print("click login")

    def test_logout(self):
        print("user logged out")