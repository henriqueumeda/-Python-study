from random import randint
from time import sleep


def sorting_values():
    sorted_numbers = []
    print('Sorting 5 numbers: ', end='')
    for i in range(0, 5):
        sorted_value = randint(1, 10)
        sorted_numbers.append(sorted_value)
        print(sorted_value, end=' ')
        sleep(0.5)
    print('DONE!')
    return sorted_numbers


def even_sum(numbers_list):
    even_total = 0
    for number in numbers_list:
        if number % 2 == 0:
            even_total += number

    print(f'The sum of the even numbers in the list {numbers_list} is: {even_total}')


numbers_list = sorting_values()
even_sum(numbers_list)
