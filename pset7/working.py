import re

# Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock.
# Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),
# wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem”
# means midday (i.e., noon).

# # Conversion Table
# # In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats
# below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized
# (with no periods therein) and that there will be a space before each. Assume that these times are representative of
# actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# Raise a ValueError instead if the input to convert is not in either of those
# formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
# But do not assume that someone’s hours will start ante meridiem and end post meridiem;
# someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see
# fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# # Either before or after you implement convert in working.py, additionally implement,
# in a file called test_working.py, three or more functions that collectively test your
# implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

#pseudocode
# define convert function
# call re.fullmatch and pass pattern, assign to match variable
# if no match raise ValueError
# extract all six groups start hour, start min, start period, end hour, end min, end period
# call to_24 for start and end times, unpack results into hour and min vars
# return formatted 24-hour string
# define to_24 helper
# validate hour is between 1 and 12, else raise ValueError
# validate minute is between 0 and 59, else raise ValueError
# if AM: hour = 0 if 12 else hour unchanged
# if PM: hour = 12 if 12 else hour + 12
# return hour, minute

# Time: O(n) re.fullmatch scans input string, scales with length of input
# Space: O(1) fixed number of variables regardless of input, no growing data structures



def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s
    )
    if not match:
        raise ValueError("Invalid format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start_hour, start_min = to_24(int(start_hour), int(start_min or 0), start_period)
    end_hour, end_min = to_24(int(end_hour), int(end_min or 0), end_period)

    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"



def to_24(hour, minute, period):
    if not (1 <= hour <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= minute <= 59):
        raise ValueError("Invalid minute")

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return hour, minute


if __name__ == "__main__":
    main()
