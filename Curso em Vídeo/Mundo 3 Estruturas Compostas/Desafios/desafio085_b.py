numbers_list = [[], []]
for counter in range(0, 7):
    number = int(input('Input an integer number: '))
    if number % 2 == 0:
        numbers_list[0].append(number)
    else:
        numbers_list[1].append(number)

numbers_list[0].sort()
numbers_list[1].sort()

print(f'The even numbers are {numbers_list[0]}')
print(f'The odd numbers are {numbers_list[1]}')
