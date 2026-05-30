import inflect

# In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu”
# means “goodbye” in French:

# Adieu, adieu, to yieu and yieu and yieu

# Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

# Adieu, adieu, to yieu, yieu, and yieu

# To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

# In a file called adieu.py, implement a program that prompts the user for names,
# one per line, until the user inputs control-d. Assume that the user will input at least one name.
# Then bid adieu to those names, separating two names with one and, three names with two commas
# and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

#pseudocode
# empty list of names
# while true loop
# open try block
# prompt for name and entitle
# add name from input to list
# except EOFError for ctrl D
# use p.join on list
# print(f "Adieu, adieu, to {result}")

# Time: O(n) joining each name in list as well as .title()
# Space: O(n) building names list scales with input

p = inflect.engine()
names = []

while True:
    try:
        text = input("Name: ").title()
        names.append(text)
    except EOFError:
        result = p.join(names)
        print(f"Adieu, adieu, to {result}")
        break
