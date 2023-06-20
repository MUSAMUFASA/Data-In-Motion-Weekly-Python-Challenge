#Create a function that returns True when num1 is equal to num2; otherwise return False

def func(num1,num2):
    if int(num1) == int(num2) and type(num1) == type(num2):
        print(True)
    else:
        print(False)


func(5,5)

