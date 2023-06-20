# #Problem: Create a function that takes in a string as an input. If the string starts with a vowel, return True. If
# not, return False.

def starts_with_vowel(word):
    vowels = ['a','e','i','o','u']
    cap_vowels = ['A','E','I','O','U']
    if type(word) == str:
        if (word[0] in vowels) or (word[0] in cap_vowels):
            print("True")
        else:
            print("False")
    else:
        print("Function only works with strings")


starts_with_vowel("hello")
starts_with_vowel("another")