initial_number = int(input('Input an integer number: '))
num = initial_number

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num //2
if isNeg:
    result = '-' + result
print(f'The binary equivalent of the decimal number {initial_number} is {result}')
