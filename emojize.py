import emoji

def main ():
    text = input("Input: ")

    output =emoji.emojize(text, language ="alias")
    print("Output: ", output)

if __name__ == "__main__":
    main()
