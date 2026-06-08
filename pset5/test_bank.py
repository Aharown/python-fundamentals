from bank import value
# in a file called test_bank.py, implement three or more functions that collectively test
# your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_bank.py

def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20

def test_other():
    assert value("yo") == 100
    assert value("what's up") == 100
