s = input("Input: ")

print("Output: ", end="")
for c in s:
    if c.lower() in ["a","e","i","o","u"]:
        continue
    print(c, end="")
print()
