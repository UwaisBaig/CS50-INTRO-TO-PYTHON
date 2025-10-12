import inflect

def main():

    p = inflect.engine()
    names = []


    while True:
        try:
            name = input().strip()
            if name:
                names.append(name)
        except EOFError:
            break

    adieu_line = p.join(names)

    print(f"Adieu, adieu, to {adieu_line}")

if __name__ == "__main__":
    main()
