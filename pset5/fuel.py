# In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

# convert expects a str in X/Y format as input, wherein X is a non-negative integer and Y is a positive integer,
# and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
# If Y is 0, then convert should raise a ZeroDivisionError.

# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise, wherein Z is that same int.

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError("Invalid fraction")
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("X cannot be greater than Y")
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
