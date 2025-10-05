def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            # Case 1: Numeric format -> M/D/YYYY
            if "/" in date:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)

                if m < 1 or m > 12 or d < 1 or d > 31:
                    raise ValueError

                print(f"{y}-{m:02}-{d:02}")
                break

            # Case 2: Written format -> Month D, YYYY
            elif "," in date:
                parts = date.split()
                month = parts[0]
                d = parts[1].replace(",", "")
                y = parts[2]

                m = months.index(month) + 1
                d, y = int(d), int(y)

                if d < 1 or d > 31:
                    raise ValueError

                print(f"{y}-{m:02}-{d:02}")
                break

        except Exception:
            continue


if __name__ == "__main__":
    main()


