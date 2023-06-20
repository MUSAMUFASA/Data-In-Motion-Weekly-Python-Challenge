def swap_key_values(original_dict):
    #STEP 1 - Extracting keys and values from input into lists, keys and values.
    values = [original_dict[value] for value in original_dict]
    keys = [key for key in original_dict]


    #STEP 2 - Creating new dictionary with keys and values swapped.
    new_dict = {}

    for each_key in range (0, len (keys)):
        new_key = values[each_key]
        new_value = keys[each_key]
        new_dict[new_key] = new_value

    print (new_dict)


original_dict = {"apple": 1, "banana": 2, "cherry": 3}

swap_key_values(original_dict)