from plates import is_valid

def test_basic():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("C") == False
    assert is_valid("CS50P") == False

def test_start_letters():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False
    assert is_valid("12AB") == False

def test_length():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_chars():
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("HELLO!") == False
