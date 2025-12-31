from fpdf import FPDF

def main():
    user_name = input("Name: ")

    pdf = FPDF(format='A4', orientation='P')
    pdf.add_page()

    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 20, "CS50 Shirtificate", align='C', ln=True)

    pdf.image("shirtificate.png", x=55, y=50, w=100)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 24)
    pdf.set_xy(0, 100)
    pdf.cell(0, 10, user_name, align='C')

    pdf.output("shirtificate.pdf")
    print("Shirtificate created!")

if __name__ == "__main__":
    main()
