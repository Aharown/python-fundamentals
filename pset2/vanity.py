# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
# with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
# or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
# Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call
# (e.g., one function per requirement).

#pseudocode
# take input
# 1 function per req
# def starts with 2 letters check first two chars are letters
# def starts with 2 letters check first two chars are letters
# def length takes input and checks that length is 2 <= len(input) <= 6
# def numbers checks that numbers with flag and for loop
# def cleanup will chain methods like strip and replace to remove spaces and punctuation
# is valid calls all functions
# main will assign input variable and call is valid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    return plate_len(plate) and starts_with_two_letters(plate) and numbers(plate)

def starts_with_two_letters(plate):
    return plate[0].isalpha() and plate[1].isalpha()

def plate_len(plate):
    return 2 <= len(plate) <= 6

def numbers(plate):
    found_digit = False
    for c in plate:
        if c.isdigit():
            if not found_digit and c == "0":
                return False
            found_digit = True
        elif found_digit:
            return False
    return True


main()
