def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x, y = int(x), int(y)

            if y == 0:
                raise ZeroDivisionError

            if x > y or y == 0 or x < 0 or y < 0:
                raise ValueError

            fuel = round((x / y) * 100)

            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{fuel}%")
            break

        except (ValueError, ZeroDivisionError):
            pass

main()
