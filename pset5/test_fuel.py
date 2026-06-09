import pytest
from fuel import convert, gauge

# Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert
# and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_fuel.py


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("abc/4")
    with pytest.raises(ValueError):
        convert("3/2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
