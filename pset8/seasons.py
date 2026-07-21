from datetime import date
import sys
import inflect

p = inflect.engine()


# Assuming there are 365 days in a year, there are 365 ×24 ×60 =525,600 minutes in that same year
# (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years?
# Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have
# 1 ×24 ×60 =1,440 additional minutes. In fact, how many minutes has it been since you were born? Well, that, too,
# depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel.
# Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class called date that can help,
# per docs.python.org/3/library/datetime.html#date-objects.

# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

# Structure your program per the below, not only with a main function but also with one or more other functions as well:

#pseudocode
# import sys
# import inflect
# initialise inflect engine

# define main
# call get_date() and assign to dob var
# call date.today() and assign to today var
# call calculate_minutes(dob, today) and assign to minutes var
# convert minutes to words using p.number_to_words() with andword=''
# capitalise and print with "minutes" appended

# define get_date
# try block
# prompt user for date of birth in YYYY-MM-DD format
# parse with date.fromisoformat()
# return parsed date
# except ValueError
# sys.exit with invalid date message

# define calculate_minutes(dob, today)
# subtract dob from today to get timedelta
# multiply .days by 24 * 60 to get total minutes
# return result

# Time: O(1) fixed number of operations regardless of input
# Space: O(1) fixed variables, no growing ds


def main():
    dob = get_date()
    today = date.today()
    minutes = calculate_minutes(dob, today)
    print(f"{p.number_to_words(minutes, andword='').capitalize()} minutes")


def get_date():
    try:
        dob = date.fromisoformat(input("Date of Birth: "))
        return dob
    except ValueError:
        sys.exit("Invalid date format")


def calculate_minutes(dob, today):
    delta = today - dob
    return delta.days * 24 * 60


if __name__ == "__main__":
    main()
