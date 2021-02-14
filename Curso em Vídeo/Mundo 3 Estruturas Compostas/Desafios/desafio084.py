people = list()
highest_weight = lowest_weight = 0
while True:
    name = input('Name: ')
    weight = float(input('Weight: '))

    if len(people) == 0:
        highest_weight = weight
        lowest_weight = weight
    else:
        if weight > highest_weight:
            highest_weight = weight
        if weight < lowest_weight:
            lowest_weight = weight

    person = [name, weight]
    people.append(person[:])
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input('Do you want to continue [Y/N]? ').strip().upper()[0]

    if answer == 'N':
        break
print('-' * 30)
print(f'There are {len(people)} people signed.')
print(f'The highest weight was {highest_weight} from ', end='')
for individual in people:
    if individual[1] == highest_weight:
        print(f'[{individual[0]}]', end=' ')

print(f'\nThe lowest weight was {lowest_weight} from ', end='')
for individual in people:
    if individual[1] == lowest_weight:
        print(f'[{individual[0]}]', end=' ')
