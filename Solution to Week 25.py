"""Write a function named only_ints that takes two parameters. Your function should return True if both parameters
are integers, and False otherwise. For example, calling only_ints(1, 2) should return True, while calling only_ints(
“a”, 1) should return False. """

def only_ints(parameter1,parameter2):
    if type(parameter1) == int and type(parameter2) == int:
        return True
    else:
        return False

results_1 = only_ints(1, 2)
results_2 = only_ints("a", 1)
print(results_1)
print(results_2)