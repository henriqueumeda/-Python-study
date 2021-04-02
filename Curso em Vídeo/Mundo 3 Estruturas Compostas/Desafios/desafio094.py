total_age = 0
people = []
while True:
    person = {}
    name = input('Name: ')
    while True:
        sex = input('Sex [M/F]: ').strip().upper()
        if sex == 'M' or sex == 'F':
            break
        print('[ERROR] Invalid sex. The valid entries for sex are only M or F.')
    is_int = False
    age = input('Age: ')
    while not is_int:
        try:
            age = int(age)
            is_int = True
        except ValueError:
            age = input('[ERROR] This was not a valid input. Please insert the age again.\nAge: ')
    while True:
        keep_asking = input('Do you want to continue? [Y/N] ').strip().upper()
        if keep_asking == 'Y' or keep_asking == 'N':
            break
        print('[ERROR] Invalid answer. Please answer only Y or N.')

    person['name'] = name
    person['sex'] = sex
    person['age'] = age
    total_age += age
    people.append(person)

    if keep_asking == 'N':
        break

average = total_age/len(people)
print('-=' * 15)
print('A) There are {} signed people.'.format(len(people)))
print('B) The average age is {:.2f}'.format(average))
print('C) The women are ', end='')
for person in people:
    if person['sex'] == 'F':
        print(person['name'], end=' ')
print('\nD) List of people above the average age:')
for person in people:
    if person['age'] > average:
        for key, value in person.items():
            print(key, '=', str(value) + ';', end=' ')
        print()
