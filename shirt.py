import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line argumnets")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_ext =[".jpg",".jpeg",".png"]

    in_ext = os.path.splitext(input_file)[1].lower()
    out_ext = os.path.splitext(output_file)[1].lower()

    if in_ext not in valid_ext:
        sys.exit("Invalid input")
    if out_ext not in valid_ext:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    image = ImageOps.fit(image, shirt.size)

    image.paste(shirt, mask=shirt)

    image.save(output_file)

if __name__ == "__main__":
    main()
