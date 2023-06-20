# Write a function called number_compare. This function takes in two parameters (both numbers). If the first is
# greater than the second, this function returns “First is greater” If the second number is greater than the first,
# the function returns “Second is greater” Otherwise the function returns “Numbers are equal”

def number_compare(number1, number2):
    if (type(number1) == int) and (type(number2) == int):
        if number1 > number2:
            print("First is greater.")
        elif number2 > number1:
            print("Second is greater.")
        else:
            print("Numbers are equal.")
    else:
        print("Function only accepts numbers.")


number_compare(50, 15)
number_compare("sdf", 15)

