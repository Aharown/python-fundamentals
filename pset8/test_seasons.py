from datetime import date
from seasons import calculate_minutes


def test_one_year():
    dob = date(2023, 1, 1)
    today = date(2024, 1, 1)
    assert calculate_minutes(dob, today) == 365 * 24 * 60


def test_leap_year():
    dob = date(2024, 1, 1)
    today = date(2024, 12, 31)
    assert calculate_minutes(dob, today) == 365 * 24 * 60


def test_one_day():
    dob = date(2025, 1, 1)
    today = date(2025, 1, 2)
    assert calculate_minutes(dob, today) == 1 * 24 * 60


def test_same_day():
    dob = date(2025, 1, 1)
    today = date(2025, 1, 1)
    assert calculate_minutes(dob, today) == 0


def test_multiple_years():
    dob = date(2023, 1, 1)
    today = date(2025, 1, 1)
    assert calculate_minutes(dob, today) == 731 * 24 * 60
