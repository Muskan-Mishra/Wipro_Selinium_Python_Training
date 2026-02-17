import pytest

@pytest.fixture(params=[1, 4, 3, 11])
def number(request):
    return request.param

def test_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
        assert number % 2 == 0
    else:
        print(f"{number} is Odd")
        assert number % 2 != 0