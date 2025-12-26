import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"

    if not re.match(pattern,ip):
        return False

    parts=ip.split(".")
    for part in parts:
        if len(part) > 1 and part[0]=="0":
            return False
        if not 0<=int(part)<=255:
            return False

    return True






if __name__ == "__main__":
    main()
