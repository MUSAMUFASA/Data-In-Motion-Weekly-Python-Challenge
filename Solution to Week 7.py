#Problem: Create a function that takes a list of dictionaries and returns the sum of people’s budgets.
def get_budgets(dictionaries):
    #Step 1 & 2 - Extract all budgets from each dictionary and append them into a list, then sum them.
    sum_budget = sum([int(each_dictionary['budget']) for each_dictionary in dictionaries])
    print(sum_budget)



