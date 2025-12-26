from working import convert
import pytest


def test_basic_conversion():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed_formats():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 PM to 2 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # bad format

    with pytest.raises(ValueError):
        convert("9AM to 5PM")  # missing spaces
