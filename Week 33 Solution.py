def loves_me(number):
    list_phrases = []
    first_phrase = "Loves me"
    second_phrase = "Loves me not"

    """STEP 0 - Defining acceptable limits of the function. If the provided number is lesser than one, the function 
    shouldn't return Loves me / Loves me not. It should tell the user to insert a feasible number"""

    if number >= 1:

        """STEP 1 - Appending "Loves me" and "Loves me not" to the empty list created above. If number in function is 
        even, the penultimate element in the list should be "Loves me not". If it is odd, the last element in the list 
        should be "Loves me"."""

        for i in range(0,number-1):
            if i % 2 == 0:
                list_phrases.append(first_phrase)
            else:
                list_phrases.append(second_phrase)

        """STEP 2 - Appending the last upper case element. If number in function is even, last element in the 
        list should be upper case "LOVES ME NOT" and if odd, last element in the list should be uppercase "LOVES ME"."""

        if number % 2 == 0:
                list_phrases.append(second_phrase.upper())
        else:
                list_phrases.append((first_phrase.upper()))

        """STEP 3 - Joining all elements in the list into a string"""

        n_string_answer = ", ".join (list_phrases)

        """STEP 4 - Adding quotation marks"""
        string_answer = f"\"{n_string_answer}\""
        print(string_answer)

    else:
        print("Insert feasible number. Number must be equal to or greater than one.")

loves_me(0)
loves_me(1)
loves_me(2)
loves_me(3)
loves_me(4)
