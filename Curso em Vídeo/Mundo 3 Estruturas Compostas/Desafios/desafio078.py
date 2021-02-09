number_list = []
for position in range(0, 5):
    number = int(input(f'Input a number for the position {position}: '))
    number_list.append(number)

print('-=' * 30)
print(f'You inserted the numbers {number_list}')
max_positions = ''
min_positions = ''
for counter, value in enumerate(number_list):
    if value == max(number_list):
        max_positions += str(counter) + '... '
    elif value == min(number_list):
        min_positions += str(counter) + '... '

print(f'The highest inserted number was {max(number_list)} in the positions {max_positions}')
print(f'The lowest inserted number was {min(number_list)} in the positions {min_positions}')
