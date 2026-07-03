from numb3rs import validate


def test_format():
    assert validate("123.123.") == False
    assert validate("12.12.3.*") == False
    assert validate("1.1.1.1.1.1.1") == False


def test_valid_addresses():
    assert validate("2.23.123.4") == True
    assert validate("6.78.96.255") == True


def test_invalid_addresses():
    assert validate("0.-1.2.3") == False
    assert validate("2399.25555.1.2") == False
    assert validate("1.1.1.1, 3.5.4.3") == False
