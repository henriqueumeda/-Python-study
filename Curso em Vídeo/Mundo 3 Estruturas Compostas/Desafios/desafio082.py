number_list = []
even_list = []
odd_list = []
while True:
    number = int(input('Input a number: '))
    number_list.append(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input('Do you want to continue [Y/N]? ').strip().upper()[0]
    if answer == 'N':
        break

print(f'The inserted numbers are {number_list}')
print(f'The inserted even numbers are {even_list}')
print(f'The inserted odd numbers are {odd_list}')
