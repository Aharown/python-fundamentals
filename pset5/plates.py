# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below,
# wherein is_valid still expects a str as input and returns True if that str meets all requirements
# and False if it does not, but main is only called if the value of __name__ is "__main__":

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


if __name__ == "__main__":
    main()
