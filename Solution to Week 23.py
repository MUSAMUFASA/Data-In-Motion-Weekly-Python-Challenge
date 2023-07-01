"""Given a person variable: person = [[“name”, “Bruce”], [“job”, “Batman”], [“city”, “Gotham”]], Create a dictionary
called answer , that makes each first item in each list a key and the second item a corresponding value. This is the
end goal: {‘name’: ‘Bruce’, ‘job’: ‘Batman’, ‘city’: ‘Gotham’} """

person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]]


key = [i[0] for i in person]
value = [i[1] for i in person]
answer = {key[i]: value[i] for i in range(len(key))}

print(answer)