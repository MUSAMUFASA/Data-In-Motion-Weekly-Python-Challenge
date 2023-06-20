##Problem 1: Write a function that takes in an integer, minutes, and converts it into seconds

##Problem 2: Write a function that takes two numbers as arguments and returns their sum.


def convert_to_min(integer):
    if (type(integer) == int):
        seconds = integer * 60
        print(f"The equivalent in seconds is {seconds}s.")
    else:
        print("Only integers allowed")

def sum_two_numbers(number1,number2):
    print("The sum of the two numbers is", number1 + number2)
