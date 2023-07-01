"""Create a function, yell, which accepts a single string argument. It should return(not print) an uppercased version
of the string with an exclamation point added at the end. For example:  yell(“go away”) # “GO AWAY!” yell(“leave me
alone”) # “LEAVE ME ALONE!” """

def yell(sing_str):
    return (f"{sing_str.upper()}" + "!")


result = yell("go away")
print(result)
