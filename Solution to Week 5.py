# Create a function that takes in a current mood and return a sentence in the following format: “Today, I am feeling
# {mood}”. However, if no argument is passed, return “Today, I am feeling neutral”.

def func(mood):
    #Step 1 - Stating condition attached to porblem statement.
    if type(mood) == str:
        print(f"Today, I am feeling {mood}.")
    else:
        print("Today, I am feeling neutral.")

func("happy")
func("sad")