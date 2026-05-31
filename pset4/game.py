import random
import sys

# I’m thinking of a number between 1 and 100…

# What is it?
# It’s 50! But what if it were more random?

# In a file called game.py, implement a program that:

# Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

#pseudocode
# while true loop
# try block
# prompt user for level level = input("Level: ")
# if input is below 1 we continue and reprompt
# random num generated random.randint(1, input)
# while true loop
# try block
# while loop
# user prompted to guess int guess = input("Guess: ")
# if guess < rand_num print("Too small!") continue
# if guess > rand_num print("Too large!") continue
# else guess == rand_num print("Just right!") sys.exit()

# Time: O(1) each operation is O(1)
# Space: O(1) fixed vars regardless of input

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
    except ValueError:
        continue
    break

rand_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
    except ValueError:
        continue

    if guess < rand_num:
        print("Too small!")
    elif guess > rand_num:
        print("Too large!")
    else:
        print("Just right!")
        sys.exit()
