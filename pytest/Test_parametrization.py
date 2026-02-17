#no parameters used
def test_add1():
    assert 2 + 3 == 5


def test_add2():
    assert 4 + 5 == 9

import pytest
@pytest.mark.parametrize("a , b , result",[
    (2,3,5),
    (4,5,9),
    (10,2,12)
])

def test_add(a,b,result):
    assert a + b == result

@pytest.mark. parametrize("number",[1,2,3,4,5])
def test_even(number):
    assert number%2 == 0

@pytest.mark.parametrize("payload", [
     {1: 'Geeks', 2: 'For', 3: 'Geeks'},
     { "name": "Kat", 1: "Python", (1, 2): [1,2,4] }


])
def test_create_user(payload):
    assert payload["age"]>18
