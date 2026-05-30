import sys
from pyfiglet import Figlet
import random

# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of
# ordinary text, a form of ASCII art:

#  _ _ _          _   _     _
# | (_) | _____  | |_| |__ (_)___
# | | | |/ / _ \ | __| '_ \| / __|
# | | |   <  __/ | |_| | | | \__ \
# |_|_|_|\_\___|  \__|_| |_|_|___/
# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
# and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.

# pseudocode
# install figlet
# import figlet
# import sys
# import random
# get font list figlet.getFonts()
# define function checks len of sys arguments
# if not == 1 | == 3 then exit with error msg
# otherwise happy path
# if len is 1 then we use random on list of fonts
# print text in output using print(figlet.renderText(s))
# if len is 3 then we set font figlet.setFont(font=f) we interpolate sys.argv[1] into set font as well as style
# print text in output using print(figlet.renderText(s))

# Time: O(n) length of input text passed to renderText()
# Space: O(n) output str scales with input str

figlet = Figlet()
font_list = figlet.getFonts()


def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        if sys.argv[2] not in font_list:
            sys.exit("Invalid usage")

    text = input("Input: ")

    if len(sys.argv) == 1:
        print(random_font(text))
    else:
        print(chosen_font(text))


def random_font(text):
    rand_font = random.choice(font_list)
    figlet.setFont(font=rand_font)
    return figlet.renderText(text)


def chosen_font(text):
    selected = sys.argv[2]
    figlet.setFont(font=selected)
    return figlet.renderText(text)


main()
