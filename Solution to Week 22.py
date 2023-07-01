"""Define a function contains_blue() that accepts any number of arguments. It should return True if any of the
arguments are “blue” (all lowercase). Otherwise, it should return False. """

def  contains_blue(*args):
    if "blue" in args:
        print("True")
    else:
        print("False")

contains_blue("blue","fsf",4,5,3,3,45,55)

