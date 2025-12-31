from datetime import date
import sys
import inflect


p = inflect.engine()

def minutes(birthday):
    today = date.today()
    delta = today - birthday
    return delta.days * 24 * 60

def main():
    birth = input("Date of Birth: ")

    try:
        year, month, day = birth.split("-")
        birthday = date(int(year), int(month), int(day))
    except Exception:
        sys.exit(1)

    mins = minutes(birthday)
    words = p.number_to_words(mins, andword="").capitalize()
    print(f"{words} minutes")


if __name__ == "__main__":
    main()
