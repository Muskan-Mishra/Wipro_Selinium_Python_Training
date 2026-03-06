#basic assertion

import pytest as check
#hard assertion = this will stop the execution of the test cases /test suite
#soft assertion will continue to run even if the assertion fails

def test_add():
    result = 2 + 3
    assert result == 5

#checking true or false
def test_boolean():
    assert True
    assert not False

#node value

def test_none():
    value = None
    assert value is None

#list assertion
def test_list():
    fruits = {"apple","banana","orange"}
    assert "banana" in fruits

#DICT assertion
def test_dict():
    creds= {"username":"admin","password":"admin123"}
    assert creds["password"] == "admin123"

#comparison lists
def test_compare():
    assert [1,2,3] == [1,2,3]


#assertion with custom message
def test_custommsg():
    result = 10
    assert result == 10 , "Result should be 5"

#soft assertion
def test_multiple():
    check.equal(1,1)
    check.equal(3,3)

def test_multiple():
    assert 1 == 2
    assert 3 == 3