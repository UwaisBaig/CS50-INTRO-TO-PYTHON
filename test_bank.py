from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello there") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("hola") == 20

def test_other_greetings():
    assert value("what's up") == 100
    assert value("good morning") == 100
    assert value("yo") == 100

def test_whitespace_and_case():
    assert value("   Hello") == 0
    assert value("  hi ") == 20
    assert value(" BYE ") == 100
