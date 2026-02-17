import pytest
def setup_function(function):
    print("opening the browser")

def teardown_function(function):
    print("closing the browser")

def testcase1():
    print("Testcase1 is exceuted")
@pytest.mark.sanity
def testcase2():
    print("Testcase2 is exceuted")
@pytest.mark.regression
def testcase3():
    print("Testcase3 is exceuted")
