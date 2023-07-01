"""Write a function that transforms a list of characters into a list of dictionaries, where: The keys are the
# characters themselves. The values are the ASCII codes of those characters."""

def transform(words):
    list_args = words
    keys = [words for words in list_args]
    values = [ord(words) for words in list_args]
    fina_dict = {keys[key_value]:values[key_value] for key_value in range(len(keys))}
    print(fina_dict)


transform(["a","c","R","T"])

