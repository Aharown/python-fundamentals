# Suppose that you’re in the habit of making a list of items you need from the grocery store.

# In a file called grocery.py, implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing
# each line with the number of times the user inputted that item. No need to pluralize the items.
# Treat the user’s input case-insensitively.

#pseudocode
# init empty dict
# reprompt user via while true loop
# try block for EOFError ctrl-d access
# assign input to item and capitalise
# check membership of item and add to count if true
# assign 1 as value if not
# EOFError
# iterate over sorted groceries keys list
# interpolate count and item

# Time: O(n log n) sorting groceries list
# Space: O(n) dict stores n items

groceries = {}

while True:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        for item in sorted(groceries):
            print(f"{groceries[item]} {item}")
        break
