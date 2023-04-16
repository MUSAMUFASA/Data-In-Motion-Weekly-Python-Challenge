def arithmetic_operation(string_number):
    ##Step 1 - Extracting integers and arithmetic operators from inputted string
    first_number = int(string_number[0:2])
    second_number = int(string_number[len(string_number)-2:len(string_number)])
    ar_operator = string_number[3:5]

    ##Step 2 - Defining the conditions
    if ar_operator == "+ ":
        print(first_number + second_number)
    elif ar_operator == "- ":
        print(first_number - second_number)
    elif ar_operator == "* ":
        print(first_number * second_number)
    elif ar_operator == "//":
        try:
            print ("%.2f" % (first_number / second_number))
        except ZeroDivisionError:
            print(-1)
    else:
        print("Insert string number as appropriate. The only valid operators are * - + and //. Also,"
              " only two numbers are accepted between 1 valid operator.")


arithmetic_operation("64 + 23")
arithmetic_operation("45 - 12")
arithmetic_operation("32 * 41")
arithmetic_operation("93 // 23")
arithmetic_operation("67 // 0")

