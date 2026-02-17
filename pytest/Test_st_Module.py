import pytest

def setup_module(module):
    print("Open the db connection")


def teardown_module(module):
    print("closing the browser")

def test_read():
    print("Reading the db")

def test_write():
    print("writing the data to the db")

def test_updating():
    print("updating the db")
