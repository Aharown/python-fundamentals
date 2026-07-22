import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_init_custom_capacity():
    jar = Jar(20)
    assert jar.capacity == 20


def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(12.5)
    with pytest.raises(ValueError):
        Jar("twelve")


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


def test_deposit_exceeds_capacity():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(6)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2


def test_withdraw_too_many():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(3)
        jar.withdraw(5)
