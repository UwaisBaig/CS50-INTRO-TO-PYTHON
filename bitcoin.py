#!/usr/bin/env python3
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        headers = {"Authorization": "Bearer:..... fill your own"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching data")

    try:
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing response")

    total = n * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
