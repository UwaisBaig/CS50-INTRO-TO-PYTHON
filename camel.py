s = input("camelCase: ").strip()
snake = ""

for c in s:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c
print("snake_case:", snake)

