def print_sum(*values):
    s = 0
    for number in values:
        s += number
    print(f'The sum of {values} is {s}')


print_sum(5, 2)
print_sum(2, 9, 4)
