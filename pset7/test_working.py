import pytest
from working import convert


def test_valid_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"



def test_midnight_and_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_late_night_hours():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("11:00 PM to 7:00 AM") == "23:00 to 07:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
    with pytest.raises(ValueError):
        convert("nine AM to five PM")
