# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one
# decimal place.


def conv_to_radians(radians):
    #Step 1 - Import math module
    import math
    #Step 2 - write equation for calculation of degrees.
    deg = round((((float(radians) * 180) / (float(math.pi)))),2)
    print(deg)


conv_to_radians(4)