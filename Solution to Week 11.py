# #Problem 1: Write two functions: to_int() : A function to convert a string to an integer.

def to_int(string_):
    try:
        str(int(string_))
    except ValueError:
        print("Only figures allowed.")
    else:
        print(str(int(string_)))


