from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25


def test_convert_error():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"   
