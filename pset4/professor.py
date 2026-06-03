import random

# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate
# ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = ,
# David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
# If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem,
# the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

# Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits.
# No need to support operations other than addition (+).
# Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to
# simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns
# 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a
# ValueError if level is not 1, 2, or 3:





#main
# call get_level once before problem loop and store in level var
# initialise score counter to 0
# for every i in range 10
#   x, y = generate_integer(level), generate_integer(level)
#   for every i in range 3
#     try block
#     set answer variable to int of user input with x and y interpolated
#     if answer is correct then increment counter by 1 and break loop
#     else print EEE
#     except value error print EEE
#   else (for/else — all 3 attempts exhausted)
#     output correct answer
# print score counter interpolated

# Time: O(1) each operation bound by fixed constants regardless of input
# Space: O(1) no growing DS, all fixed

def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}/10")



#get_level
# while true loop
# try block (value error)
# store user input in level var
# check if level has membership in 1-3 list
# if not continue to top of loop for reprompt

def get_level():
    while True:
       try:
           level = int(input("Level: "))
           if level in [1, 2, 3]:
               return level
       except ValueError:
           pass


#generate_integer
# receives level
# checks that level has membership if not raise value error
# associate levels with ranges of numbers
# if 1, reassign var with 0-9. if 2 we reassign var to 10-99. 3 we reassign var to 100-999
# return var

def generate_integer(level):
    match level:
        case 1:
            level = random.randint(0, 9)
        case 2:
            level = random.randint(10, 99)
        case 3:
            level = random.randint(100, 999)
        case _:
            raise ValueError("Wrong level")
    return level



if __name__ == "__main__":
    main()
