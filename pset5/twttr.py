# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
# restructuring your code per the below, wherein shorten expects a str as input and returns
# that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    word = input("Input: ").lower()
    print(shorten(word))

def shorten(word):
     result = ""
     vowels = "AEIOUaeiou"

     for c in word:
          if c not in vowels:
               result += c
     return result



if __name__ == "__main__":
     main()
