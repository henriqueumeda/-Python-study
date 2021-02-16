matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even_sum = third_column_sum = 0
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Input the value of the position [{line}:{column}]: '))
        if matrix[line][column] % 2 == 0:
            even_sum += matrix[line][column]
        if column == 2:
            third_column_sum += matrix[line][column]
        if line == 1 and column == 0:
            second_line_highest = matrix[line][column]
        elif line == 1 and matrix[line][column] > second_line_highest:
            second_line_highest = matrix[line][column]

print('-=' * 15)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[ {matrix[line][column]:^5} ]', end='')
    print()
print('-=' * 15)
print(f'The sum of the values is {even_sum}')
print(f'The sum of the values of the third column is {third_column_sum}')
print(f'The highest number of the second line is {second_line_highest}')
