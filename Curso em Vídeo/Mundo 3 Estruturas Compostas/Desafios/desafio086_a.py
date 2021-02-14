matrix = []
for line in range(0, 3):
    for column in range(0, 3):
        number = int(input(f'Input a number to the position [{line}:{column}]: '))
        matrix.append([line, column, number])
print('-=' * 15, end='')

for counter in range(0, 9):
    if matrix[counter][0] != matrix[counter-1][0]:
        print('')
    print(f'[{matrix[counter][2]:3}:^5]', end='')
