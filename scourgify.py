import sys
import csv

def main():

    if len(sys.argv)!=3:
        sys.exit("Too few command-line arguments")

    input_file=sys.argv[1]
    output_file=sys.argv[2]

    students = []

    try:
        with open(input_file) as input_csv:
            reader= csv.DictReader(input_csv)

            for row in reader:
                last,first=row["name"].split(", ")
                students.append({
                    "first":first,
                    "last":last,
                    "house":row["house"]
                })
    except FileNotFoundError:
        sys.exit("Could not read{input_file}")

    with open(output_file,"w",newline="") as output_csv:
        writer=csv.DictWriter(output_csv,fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)

if __name__=="__main__":
    main()

