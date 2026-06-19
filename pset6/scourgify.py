import sys
import csv

# Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent,
# if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:
# name,house
# "Abbott, Hannah",Hufflepuff
# "Bell, Katie",Gryffindor
# "Bones, Susan",Hufflepuff
# "Boot, Terry",Ravenclaw
# "Brown, Lavender",Gryffindor
# "Bulstrode, Millicent",Slytherin
# "Chang, Cho",Ravenclaw
# "Clearwater, Penelope",Ravenclaw
# "Crabbe, Vincent",Slytherin
# "Creevey, Colin",Gryffindor
# "Creevey, Dennis",Gryffindor
# "Diggory, Cedric",Hufflepuff
# "Edgecombe, Marietta",Ravenclaw
# "Finch-Fletchley, Justin",Hufflepuff
# "Finnigan, Seamus",Gryffindor
# "Goldstein, Anthony",Ravenclaw
# "Goyle, Gregory",Slytherin
# "Granger, Hermione",Gryffindor

# Even though each “row” in the file has three values (last name, first name, and house), the first two are
# combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space.
# Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

# Dear Potter, Harry,

# Rather than with, for instance:

# Dear Harry,

# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name.
# Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read,
# the program should exit via sys.exit with an error message.

# Time: O(n) due to looping over every row in CSV
# Space: O(n) due to ouput file

#pseudocode
# import sys
# import csv
# define get files function
# check argv length, if < 3 sys.exit with msg, if > 3 sys.exit with msg
# return both files as tuple
# define main
# unpack tuple
# with block and open first csv file
# assign reader variable and use dictreader
# open another with block and open second csv file remember to pass "w" when opening
# assign writer and fieldnames vars
# loop over reader
# split names parallel assignment
# write rows for output csv
# except FileNotFoundError with sys.exit


def main():
    before_csv, after_csv = get_files()
    try:
        with open(before_csv) as before_file:
            reader = csv.DictReader(before_file)
            with open(after_csv, "w") as after_file:
                writer = csv.DictWriter(
                    after_file, fieldnames=["first", "last", "house"]
                )
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )
    except FileNotFoundError:
        sys.exit(f"Could not read {before_csv}")


def get_files():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()
