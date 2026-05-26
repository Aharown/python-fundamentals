# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order,
# which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
# Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
# Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636
# could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted
# in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits,
# and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
# in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any
# of the values in the list below:

# [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
# prompt the user again. Assume that every month has no more than 31 days;
# no need to validate whether a month has 28, 29, 30, or 31 days.

#pseudocode
# init months dictionary mapping month names to numbers
# main():
# while true loop for reprompting
#   get user input "Date: "
#   if any month name in input call word_date(date)
#   else call number_date(date)
#   if result is not None print result and break

# word_date(date):
#   try:
#     remove comma from date
#     unpack into month, day, year via split()
#     if month not in months dict return None
#     look up month number from dict
#     convert day and year to int
#     validate day is between 1 and 31 return None if not
#     return f"{year:04}-{month:02}-{day:02}"
#   except ValueError return None

# number_date(date):
#   try:
#     unpack into month, day, year via split("/")
#     convert all three to int
#     validate month between 1-12 and day between 1-31 return None if not
#     return f"{year:04}-{month:02}-{day:02}"
#   except ValueError return None

# Time: O(1) fixed number of entries
# Space: O(1) dict doesn't grow always 12 

months = {
    "January": 1, "February": 2, "March": 3,
    "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}


def main():
    while True:
        date = input("Date: ")
        if any(month in date for month in months):
            result = word_date(date)
        else:
            result = number_date(date)
        if result:
            print(result)
            break


def word_date(date):
    try:
        date = date.replace(",", "")
        month, day, year = date.split()
        if month not in months:
            return None
        month = months[month]
        day, year = int(day), int(year)
        if not 1 <= day <= 31:
            return None
        return f"{year:04}-{month:02}-{day:02}"
    except ValueError:
        return None


def number_date(date):
    try:
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)
        if not 1 <= month <= 12 or not 1 <= day <= 31:
            return None
        return f"{year:04}-{month:02}-{day:02}"
    except ValueError:
        return None


main()
