from datetime import date
from seasons import minutes


def test_one_year_old():
    today = date.today()
    birthday = date(today.year - 1, today.month, today.day)

    assert minutes(birthday) == 525600 or minutes(birthday) == 527040


def test_two_years_old():
    today = date.today()
    birthday = date(today.year - 2, today.month, today.day)

    assert minutes(birthday) == 1051200 or minutes(birthday) == 1052640
