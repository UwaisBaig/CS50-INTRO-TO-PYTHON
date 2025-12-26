from numb3rs import validate


def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_invalid_numbers():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("999.999.999.999") == False


def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("...") == False
    assert validate("hello") == False
    assert validate("1.2.3.") == False
    assert validate(".1.2.3") == False
