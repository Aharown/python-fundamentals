import pytest
from twttr import shorten

# Implement one or more functions that collectively test your implementation of
# shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_twttr.py


def test_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"


def test_only_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
