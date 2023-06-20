#Problem: Create a function that takes a string as input and capitalizes the string.

def capitalise(word):
    if type(word) == str:
        print(word.capitalize())
    else:
        print("Function only works for words")


capitalise('kawu')