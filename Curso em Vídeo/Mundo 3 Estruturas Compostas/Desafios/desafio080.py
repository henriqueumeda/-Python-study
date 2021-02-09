number_list = list()
for elements in range(0, 5):
    number = int(input('Input a number: '))
    if elements == 0 or number > number_list[-1]:
        number_list.append(number)
        print(f'Number {number} inserted at the end of the list...')
    else:
        for position, value in enumerate(number_list):
            if number <= value:
                number_list.insert(position, number)
                print(f'Number {number} inserted at the position {position}')
                break

print(f'The sorted list is {number_list}')
