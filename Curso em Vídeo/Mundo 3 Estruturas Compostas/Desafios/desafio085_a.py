even = []
odd = []
for counter in range(1, 8):
    number = int(input('Input an integer number: '))
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
even.sort()
odd.sort()

print(f'The even numbers are {even}')
print(f'The odd numbers are {odd}')
