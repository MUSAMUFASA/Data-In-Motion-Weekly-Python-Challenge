# Step 0 - Identifying trends in different words that end with "ing"
vowels = ["a", "e", "i", "o", "u"]
consonants = ["r", "n","p", "x"]
consonants_also_special = ["d"]
special_phrases = ["it", "nc", "rg", "ir", "dl", "th", "zl", "lv","tl"]
special2_phrases = ["ea","ee"]
special3_phrases = ["mit"]
special4_phrases = ["idi"]
repeated_consonants = ["l", "s"]


# Step 1 - Function accepts string containing "ing" and "non-ing" words and converts string into list with each word
# as an element
def stemming(input_string):
    list_string = input_string.split (" ")
    new_list_string = []
    # Step 2 - Appending words not ending with "ing" into the list, new_list_string. This is the list that stores
    # stems resulting from first stage processing occurs. Words with less than 3 letters are also appended.
    for each_word in list_string:
        if (len(each_word) <= 3) or (each_word[-3:] != "ing"):
            new_list_string.append (each_word)
    # Step 2a - Appending stems of unique "ing words" like "baking", "sliding" that have stems - bakE, slidE.
        else:
            if (each_word[-5] in vowels) and (each_word[-4] not in consonants) and (each_word[-6:-4]
                                                                                    not in special2_phrases) and (
                    each_word[-6:-3] not in special3_phrases):
                stem = each_word[0:(len (each_word) - 3)] + "e"
                new_list_string.append (stem)
            # Step 2b - Appending stems of unique "ing words" like "cursing", "teasing" that have stems - curse, tease.
            elif (each_word[-4] == "s") and (each_word[-5] != "s"):
                stem = each_word[0:(len (each_word) - 3)] + "e"
                new_list_string.append (stem)
            # Step 2c - Appending stems of unique "ing words" like "guzzling", "dazzling" that have stems - guzzle,
            # dazzle.
            elif (each_word[1] == "u") and (each_word[-4] == "l"):
                stem = each_word[0:(len (each_word) - 3)] + "e"
                new_list_string.append (stem)
            # Step 2d - Appending stems of other unique "ing words" like "emerging", "retiring", "writing",
            # "soothing", "mincing" that have stems - emerge, retire, write, soothe ETC.
            elif (each_word[-5:-3] in special_phrases) and (each_word[-6:-3] not in special3_phrases):
                stem = each_word[0:(len (each_word) - 3)] + "e"
                new_list_string.append (stem)
            else:
                stem = each_word[0:(len (each_word) - 3)]
                new_list_string.append (stem)

    # Step 3 - Moving stems into new list (final_list_string) for final processing
    final_list_string = []
    for each_word_f in new_list_string:
    # Step 3a - Appending simple stems where the last and penultimate elements aren't the same e.g Dazzle, eat, emerge.
        if (len(each_word_f) <= 3) or (each_word_f[-2] != each_word_f[-1]):
            final_list_string.append (each_word_f)
        else:
    # Step 3b - Appending simple stems where the last and penultimate elements are the same e.g. CUTT.
            if each_word_f[-1] not in repeated_consonants:
                stem_updated = each_word_f[0:(len (each_word_f) - 1)]
                final_list_string.append (stem_updated)
    # Step 3c - Appending simple stems where the last and penultimate elements are the same e.g. chill, hiss, process.
            else:
                final_list_string.append (each_word_f)

    # Step 4 - Joining elements of list into a string

    string_return = " ".join(final_list_string)

    print(string_return)


stemming ("I am running on the beach and feeling amazing")
stemming ("recommissioning commercializing pamphleteering hardening multiprocessing wrestling breaking")
