import pytest
@pytest.mark.xfail(reason="known bug in the third-party library")
def test_function_with_bug():
    assert (1 + 1) == 3
@pytest.mark.sanity
def testcase1():
    print("Testcase1 is exceuted")
@pytest.mark.regression
def testcase2():
    print("Testcase2 is exceuted")
@pytest.mark.db
def testcase3():
    print("Testcase3 is exceuted")
