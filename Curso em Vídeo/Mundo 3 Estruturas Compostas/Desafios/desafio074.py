from random import randint
tupla = ()
print('Os valores sorteados foram: ', end='')
for contador in range(0, 5):
    numero = randint(1, 10)
    tupla += (numero, )
    print(numero, end=' ')

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
