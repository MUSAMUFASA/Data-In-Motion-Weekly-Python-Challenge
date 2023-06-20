
def pluralize(**kwargs):
    lst_words = []

    number_of_words = int(input("How many words would you like to pluralize?\n"))
    print("Type your words")
    for i in range(0,number_of_words):
        words = input ("")
        lst_words.append(words)

    plural_lst_words = []
    for i in lst_words:
        if lst_words.count(i) > 1:
            cap_i = i + "s"
            plural_lst_words.append(cap_i)

    set_words = set(plural_lst_words)
    print(set_words)

