#Problem: Create a function that takes a number num and returns its length.

def number_length(num):
    if type(num) == int:
        str_form = str(num)
        length = len(str_form)
        print(length)
    else:
        print("Function takes only numbers")

number_length(10)
number_length(5000)
