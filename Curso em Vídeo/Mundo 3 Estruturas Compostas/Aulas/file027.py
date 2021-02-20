people = {'name': 'Henrique', 'sex': 'M', 'age': 24}
print(f'{people["name"]} is {people["age"]} years old')
print(people.keys())
print(people.values())
print(people.items())

for key, values in people.items():
    print(f'{key} = {values}')

del people['sex']
print(people)

people['name'] = 'Gustavo'
people['weight'] = 59
print(people)
