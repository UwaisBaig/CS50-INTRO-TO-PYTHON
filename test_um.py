from um import count

def test_basic():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_sentence():
    assert count("Hello, um, world") == 1
    assert count("Um, yes, um, okay") == 2
    assert count("um?") == 1
    assert count("...um...") == 1

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("aluminum") == 0
