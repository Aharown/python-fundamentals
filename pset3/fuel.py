# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full,
# 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage
# rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate
# that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

#pseudocode
# break up into helper functions
# 1. validates fraction (use while true loop to reprompt user for input)
# 2. converts fraction to percentage takes the input from fraction verification function
# fraction input for user x(0+)/y(1+)
# transform fraction to percentage rounded to nearest int
# output is 1 or less, print "E"
# output is 99 or more, print "F"
# else take user input again
# catch exceptions where you expect bugs may arise such as transforming fraction to rounded whole number or if the denominator is 0

def main():
    x, y = get_fraction()
    percentage = converts(x, y)
    
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            if x > y:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return x, y


def converts(x, y):
    return round(x / y * 100)


main()
