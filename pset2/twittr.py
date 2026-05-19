# When texting or tweeting, it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
# implement a program that prompts the user for a str of text and then outputs that same text but with all vowels
# (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

#pseudocode
# take input
# var assigned vowels
# empty str for result
# iterate over input
# if char is not in vowels, append to result
# return result str

input = input("Input: ")
vowels = "AEIOUaeiou"
result = ""

for c in input:
    if c not in vowels:
        result += c

print(result)
