#fixture dependency -the second fixture will work only when the first

import pytest

def test(fixture_b):
    assert fixture_b == "Data from A + Data from B"

#fixture_b automatically receives the value returned by fixture_a.