
import pytest
def div(a,b):
    return a/b

def test_div_zero():
    with pytest.raises(ValueError) as exc_Info:
        print(exc_Info)
        div(5,0)
        assert str(exc_Info.value) == "ZeroDivisionError : division by zero"