numero = -1
while numero < 0:
    numero = int(input('Digite um número natural: '))

print('{}!='.format(numero), end='')
fatorial = 1
for contador in range(numero, 0, -1):
    print('{}'.format(contador), end='')
    if contador > 1:
        print('x', end='')
    else:
        print('=', end='')
    fatorial *= contador

print('{}'.format(fatorial))