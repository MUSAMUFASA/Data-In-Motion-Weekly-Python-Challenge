def letters(*strings):
    # STEP 1 - Appending inputted words into a string, titled list_of_strings. Also, stating limitation of function;
    # Arguments shouldn't be more than two strings.
    list_of_strings = []
    if len (strings) == 2:
        for each_word in strings:
            list_of_strings.append (each_word)
    else:
        print ("Only two elements allowed")


    # STEP 2 - Separating list_of_strings into two different lists, each containing the letters of each word.
    first_string = list (list_of_strings[0])
    second_string = list (list_of_strings[1])

    # STEP 3a - Appending letters shared by the two words into new list: sort_shared_list.
    sort_shared_list = []
    for each_letter_f in first_string:
        for each_letter_s in second_string:
            if each_letter_f == each_letter_s:
                sort_shared_list.append (each_letter_f)
    # STEP 3b - Removing duplicates from sort_shared_list via conversion to set and then converting back to list for
    # sorting.
    unique_shared_list = set (sort_shared_list)
    final_shared_list = sorted (list (unique_shared_list))

    # STEP 4a - Appending letters unique to the first word into a new list: unique_list_1.
    unique_list_1 = []
    for each_letter_f in first_string:
        if each_letter_f not in sort_shared_list:
            unique_list_1.append (each_letter_f)
    # STEP 4b - Removing duplicates from unique_list_1 via conversion to set and then converting back to list for
    # sorting.
    unique_unique_list_1_list = set (unique_list_1)
    final_unique_list_1_list = sorted (list (unique_unique_list_1_list))

    # STEP 5a - Appending letters unique to the second word into a new list: unique_list_2.
    unique_list_2 = []
    for each_letter_s in second_string:
        if each_letter_s not in sort_shared_list:
            unique_list_2.append (each_letter_s)
    # STEP 4b - Removing duplicates from unique_list_2 via conversion to set and then converting back to list for
    # sorting.
    unique_unique_list_2_list = set (unique_list_2)
    final_unique_list_2_list = sorted (list (unique_unique_list_2_list))

    # STEP 6 - Joining letters of each category into a new list: final_list.
    final_list = ["".join (final_shared_list), "".join (final_unique_list_1_list), "".join (final_unique_list_2_list)]
    print (final_list)


letters ("sharp", "soap")
letters ("board", "bored")
letters ("happiness", "envelope")
letters ("kerfuffle", "fluffy")
letters ("match", "ham")
