def highest_number(*values):
    print('-=' * 20)
    print('Analysing the inserted values...')

    if len(values) == 0:
        print('No number was informed.')
        return

    for number in values:
        print(number, end=' ')
    print()
    print(f'{len(values)} numbers were inserted.')
    print(f'The highest number was {max(values)}.')


highest_number(2, 9, 4, 5, 7, 1)
highest_number(4, 7, 0)
highest_number(1, 2)
highest_number()
