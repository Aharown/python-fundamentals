import re

# # It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word.
# # The more you do it, though, the more noticeable it tends to be!

# # In a file called um.py, implement a function called count that expects a line of text as
# input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively,
# as a word unto itself, not as a substring of some other word. For instance, given text like hello, um, world,
# the function should return 1. Given text like yummy, though, the function should return 0.

# # Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.


#pseudocode
# define count function
# call re.findall with \b word boundary pattern and re.IGNORECASE
# return length of resulting list

# Time: O(n) re.findall scans input string, scales with length of input
# Space: O(n) findall returns a list of all matches, scales with number of matches


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
