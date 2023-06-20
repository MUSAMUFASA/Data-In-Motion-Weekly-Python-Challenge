# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6
# digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if
# it’s not.

def is_valid_PIN(number):
    try:
        int(number)
    except ValueError:
        print("False")
    else:
        if ((len(number) == 4) or (len(number) == 6)):
            print("True")
        else:
            print("False")



