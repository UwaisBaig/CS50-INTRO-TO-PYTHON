import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            continue

    secret = random.randint(1,n)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0:
                continue

            if guess < secret:
                print("Too small!")

            elif guess > secret:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()
