number_list = []
while True:
    number = int(input('Input a number: '))
    if number in number_list:
        print(f'Number {number} is already on the list. Value not inserted!')
    else:
        number_list.append(number)
        print(f'Number {number} successfully inserted on the list.')
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input('Do you want to continue [Y/N]? ').strip().upper()[0]
    if answer == 'N':
        break

print('-=' * 30)
print(f'You inserted the numbers {sorted(number_list)}')