# Problem: Create a function that takes a list of strings as input. Join each string in the list to create and return
# one complete string. Each word should have a space between them.

def join(list_strings):
    new_list = ' '.join(list_strings)
    print(new_list)

join(["Hello", "how", "are", "you?"])
join(["What’s", "your", "name?"])