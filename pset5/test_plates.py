from plates import is_valid

# In a file called test_plates.py, implement four or more functions that collectively test your implementation
# of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_plates.py


def test_valid():
    assert is_valid("AAA222") == True
    assert is_valid("BE5555") == True
    assert is_valid("CI3000") == True


def test_too_low():
    assert is_valid("") == False
    assert is_valid("A") == False


def test_too_many():
    assert is_valid("AAA222222") == False


def test_no_delimeters():
    assert is_valid("AA3,000") == False
    assert is_valid("CIE!000") == False


def test_starts_with_two_letters():
    assert is_valid("A1234") == False
    assert is_valid("12345") == False


def test_numbers_at_end():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
