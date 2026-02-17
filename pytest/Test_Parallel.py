import pytest
def testcase1():
    print("Testcase1 is exceuted")

def testcase2():
    print("Testcase2 is exceuted")

def testcase3():
    print("Testcase3 is exceuted")


def testcase4():
    print("Testcase4 is exceuted")

def testcase5():
    print("Testcase5 is exceuted")




def test_login():
    print("Login test is executed")

def test_api(api_url):
    assert "https" in api_url

