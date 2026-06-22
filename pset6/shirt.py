import sys
from PIL import Image
from PIL import ImageOps
# After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt.
# No need to buy one online,but like to try one on virtually?

# In a file called shirt.py, implement a program that expects exactly two command-line arguments:

# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background) on the input after resizing
# and cropping the input to be the same size, saving the result as its output.

# Open the input with Image.open,per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
# resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
# using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
# and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

# The program should instead exit via sys.exit:

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.
# Assume that the input will be a photo of someone posing in just the right way,
# like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.


#pseudocode
# import sys
# from PIL import Image
# define get files function for validation purposes
# consider ALL validation criteria above
# return files as tuple
# Remember FileNotFoundError
# define main
# unpack inputs from tuple by calling function
# now open input file using with block
# resize inside with block
# overlay shirt png image paste
# save file using the same file name as output file

def main():
    input_file, output_file = get_files()
    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input file not found")

    shirt = Image.open("shirt.png")
    fitted = ImageOps.fit(image, shirt.size)
    fitted.paste(shirt, shirt)
    fitted.save(output_file)


def get_files():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    extensions = [".jpg", ".jpeg", ".png"]
    input_file, output_file = sys.argv[1], sys.argv[2]

    input_ext = "." + input_file.lower().split(".")[-1]
    output_ext = "." + output_file.lower().split(".")[-1]

    if input_ext not in extensions or output_ext not in extensions:
        sys.exit("Invalid file type")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    return input_file, output_file


if __name__ == "__main__":
    main()
