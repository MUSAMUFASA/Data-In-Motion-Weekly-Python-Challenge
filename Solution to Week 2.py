#Create a function that takes a string and returns the number (count) of vowels contained within it.

def num_vowels(word):
    #Step 1 - List all vowels in a list (Capital and lower cases for edge cases)
    vowels = ["a", "e", "i", "o", "u"]
    upper_vowels = ["A","E","I","O","U"]

    #Step 2 - Initialize a counter to count the number of vowels
    count = 0

    #Step 3 - Stating condition for the function to only run if a true word has been provided.
    if (type(word) == str):
    #Step 4 - Loop through the word and add to count the number of occurences for vowels.
        for each_letter in word:
            if (each_letter in vowels) or (each_letter in upper_vowels):
                count += 1
        print(count)
    else:
        print("Function only works for words")


num_vowels("NUMMMMM")