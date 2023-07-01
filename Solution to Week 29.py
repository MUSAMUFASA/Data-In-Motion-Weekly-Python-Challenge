"""Hard: Create a function that counts the number of digits in a number. Conversion of the number to a string is not
allowed. """

def count_number(number):
    if type(number) == int:
        if number > 0:
            n = abs(number)
            count = 0
            while n > 0:
                count += 1
                n //= 10
            print(count)
        elif number == 0:
            print(1)
    else:
        print("Function only accepts digits")

count_number(4556)