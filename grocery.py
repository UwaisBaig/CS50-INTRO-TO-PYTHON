def main():
    groceries = {}

    # Keep asking for items until user presses Ctrl+D (EOF)
    while True:
        try:
            item = input().strip().lower()  # Normalize to lowercase
            if item:
                groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            break

    # Sort alphabetically and print results
    for item in sorted(groceries.keys()):
        print(f"{groceries[item]} {item.upper()}")


if __name__ == "__main__":
    main()
