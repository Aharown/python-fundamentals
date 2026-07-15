from um import count


def test_um_alone():
    assert count("um") == 1
    assert count("hello, um, world") == 1


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_not_substring():
    assert count("yummy") == 0
    assert count("drummer") == 0
    assert count("umbrella") == 0
