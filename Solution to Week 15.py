# Create a function that takes a single string as argument and returns an ordered list containing the indices of all
# capital letters in the string.

def index_of_caps(orderd_list):
    correct = []
    for i in orderd_list:
        if i.isupper() == True:
            correct.append(orderd_list.index(i))
    print(correct)


index_of_caps("eDaBiT")
index_of_caps("eQuINoX")
index_of_caps("determine")