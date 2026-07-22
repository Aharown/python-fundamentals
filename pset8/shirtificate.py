from fpdf import FPDF

# Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt,
# shirtificate.png, customized with a user’s own name.

# In a file called shirtificate.py, implement a program that prompts the user for their name and outputs,
# using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.
# All other details we leave to you. You’re even welcome to add borders, colors, and lines.
# Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

# Before writing any code, do read through fpdf2’s tutorial to learn how to use it.
# Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.


#pseudocode
# def main
# prompt user for name
# call create_shirtificate(name)

# def create_shirtificate(name)
# init fpdf with portrait orientation and A4 format
# add page

# set font to Helvetica bold 36
# set text color to black
# add centered cell with "CS50 Shirtificate" title

# calculate x position to centre image on 210mm wide page
# add shirt image at calculated x, fixed y, fixed width

# set font to Helvetica bold 24
# set text color to white
# set y position over the shirt graphic
# add centered cell with name
# output to shirtificate.pdf

# Time: O(1) fixed number of operations regardless of input
# Space: O(1) fixed variables, no growing ds


def main():
    name = input("Name: ")
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()


    pdf.set_font("Helvetica", "B", 36)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


    img_width = 190
    img_x = (210 - img_width) / 2
    pdf.image("shirtificate.png", x=img_x, y=50, w=img_width)


    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(150)
    pdf.cell(0, 10, name, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
