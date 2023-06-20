# Problem: Create a function that takes in a string as an input. If the string starts with a vowel, return True. If
# not, return False.

def starts_with_vowel(word):
    #Step 1 - Stating vowels in two lists
    vowel = ['a','e','i','o','u']
    cap_vowel = ['A','E','I','O','U']

    #Step 2 - Stating condition atttached to the problem statement.
    if type(word) == str:
        if (word[0] in vowel) or (word[0] in cap_vowel):
            print("True")
        else:
            print("False")
    #Step 3 - Returning an alternative to when words aren't provided for the function.
    else:
        print("Function only works for words.")


starts_with_vowel('hello')
starts_with_vowel('Eello')