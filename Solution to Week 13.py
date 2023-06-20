# #Problem: Create a function that takes a number as its only argument and returns True if it’s less than or equal to
# zero, otherwise return False.

def less_than_or_equal_to_zero(number):
    if type(number) == int:
        if number <= 0:
            print(True)
        else:
            print("False")
    else:
        print("Only accepts integers")

less_than_or_equal_to_zero(0)
less_than_or_equal_to_zero(5)