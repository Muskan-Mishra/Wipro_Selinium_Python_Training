import pytest

@pytest.fixture(params=["chrome", "firefox"])
def testbrowser(request):
    if request.param == "chrome":
        print("Invoke chrome browser")
    else:
        print("Invoke firefox browser")