# Problem: Create a function that takes a list of non-negative integers and strings and return a new list without the
# strings.

def filter_list(list_collective):
    list_without_str = [each_element for each_element in list_collective if type(each_element) != str]
    print(list_without_str)

filter_list([1, 2, "a", "b"])
filter_list([1, 2, "aasf", "1", "123", 123])
