import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, ap1, h2, m2, ap2 = match.groups()

    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    if not (0 <= int(m1) <= 59 and 0 <= int(m2) <= 59):
        raise ValueError("Invalid minutes")

    h1_24 = to_24(int(h1), ap1)
    h2_24 = to_24(int(h2), ap2)

    if not (0 <= int(h1) <= 12 and 0 <= int(h2) <= 12):
        raise ValueError("Invalid hour")

    return f"{h1_24:02}:{m1} to {h2_24:02}:{m2}"


def to_24(hour, period):
    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour")

    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()
