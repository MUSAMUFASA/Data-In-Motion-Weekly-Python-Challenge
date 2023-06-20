# #Problem 1: Given a list [“Elie”, “Tim”, “Matt”], create a variable called answer, which is a new list containing
# the first letter of each name in the list.

ord_list = ["Elie", "Tim", "Matt"]

answer = [each_word[0] for each_word in ord_list]

print(answer)

##Problem 2: Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.

org_list = [1,2,3,4,5,6]
answer2 = [each_number for each_number in org_list if each_number % 2 == 0]

print(answer2)