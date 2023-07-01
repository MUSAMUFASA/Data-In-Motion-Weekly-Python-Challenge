"""Create a function that takes a list of numbers and a string and return a list of numbers as per the following rules:
“Asc” returns a sorted list in ascending order.
“Des” returns a sorted list in descending order.
“None” returns a list without any modification."""

def multi(list_w,str_w):
    if (type(list_w) == list):
        if str_w == "Asc":
            print (sorted (list_w, reverse=False))
        elif str_w == "Des":
            print (sorted (list_w, reverse=True))
        elif str_w == None:
            print (list_w)
        else:
            print ("Use correct keywords please")
    else:
        print("First parameter must be a list of numbers")

