## Create a function that creates a box based on dimension n.

def make_box(number):
    if number > 1:
        mini_box = "#"

        #The Final box having dimension, number
        Pseudo_Entire_Box = []
        Entire_Box = []

        #Step 1 - Create first & last line

        for i in range(number):
            Pseudo_Entire_Box.append(mini_box)
        first_last_line = ''.join(Pseudo_Entire_Box)
        Entire_Box.insert(1,first_last_line)
        Entire_Box.insert (0, first_last_line)

        #Step 2 - Create Middle Lines
        Pseudo_Middle_line = []
        Middle_line = []
        Empty_space = " "
        number_of_partial_spaces = number - 2
        for i in range(number_of_partial_spaces):
            Pseudo_Middle_line.append(Empty_space)
        Pseudo_Middle_line.insert (0, mini_box)
        Pseudo_Middle_line.insert (number, mini_box)
        Middle_line = ''.join(Pseudo_Middle_line)


        #Step 3 - Putting it together (raw form)
        for i in range(1,number-1):
            Entire_Box.insert(i,Middle_line)

        #Step 4 - Arranging neatly
        for i in Entire_Box:
            print(i)
    elif number == 1:
        print("#")
    else:
        print("Please insert a feasible number of dimensions")



