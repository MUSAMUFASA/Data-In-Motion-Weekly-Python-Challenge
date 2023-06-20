# Create a function that takes a number as its only argument and returns True if it’s less than or equal to zero,
# otherwise return False.

def func(number):
    #Step 1 - Stating condition attached to problem statment.
    if (type(number) == int) and (number <=0):
        print(True)
    else:
        print(False)

func("")
func(0)