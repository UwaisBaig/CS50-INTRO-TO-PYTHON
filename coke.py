total_coins = 50
print("Amount Due: ",total_coins)


while(total_coins > 0):
    coins = int(input("Insert Coin: "))

    if coins in [25, 10, 5]:
        total_coins -= coins

    if total_coins > 0:
        print("Amount Due:",total_coins)
    else:
        print("Change Owed:",abs(total_coins))


