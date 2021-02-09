number_list = list()
while True:
    number = int(input('Input a number: '))
    answer = ''
    number_list.append(number)
    while answer != 'N' and answer != 'Y':
        answer = input('Do you want to continue [Y/N]? ').strip().upper()[0]
    if answer == 'N':
        break

if 5 in number_list:
    existing_five = 'is'
else:
    existing_five = "isn't"

print(f'You inserted {len(number_list)} elements.')
number_list.sort(reverse=True)
print(f'The values inserted in descending order is {number_list}')
print(f'The number 5 {existing_five} in the list.')
