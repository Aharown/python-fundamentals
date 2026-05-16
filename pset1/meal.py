# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00,
# lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
# Wouldn’t it be nice if you had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs
# whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as
# #:## or ##:##. And assume that each meal’s time range is inclusive.
#  For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main)
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

# pseudocode
# get user input (input will be in 24 hour str format)
# convert function needs to convert 24 hour str format to a float
# split the input str into hours and minutes (parallel assignment)
# convert str to ints (parallel assignment)
# get float by dividing minutes by 60
# converted time is hours + float
# use comparison operators: if time >= 7 && <= 8 print(breakfast time)


def main():
    time = input("What time is it? ")
    converted = convert(time)

    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")

        
def convert(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)
    converted_mins = float(minutes / 60)
    converted_time = hours + converted_mins

    return converted_time


if __name__ == "__main__":
    main()
