import pytest

# -------- function level --------
@pytest.fixture(scope="function")
def openbrowser():
    print("\nopen browser")

@pytest.fixture(scope="function")
def closebrowser():
    print("close browser")


# -------- class level --------
@pytest.fixture(scope="class")
def openbrowser_class():
    print("\nopen browser (class)")

@pytest.fixture(scope="class")
def closebrowser_class():
    print("close browser (class)")


# -------- module level --------
@pytest.fixture(scope="module")
def openbrowser_module():
    print("\nopen browser (module)")

@pytest.fixture(scope="module")
def closebrowser_module():
    print("close browser (module)")


# -------- session level --------
@pytest.fixture(scope="session")
def openbrowser_session():
    print("\nopen browser (session)")

@pytest.fixture(scope="session")
def closebrowser_session():
    print("close browser (session)")