numero = int(input('Digite um número inteiro: '))
contador = 0
for divisor in range(1, numero+1):
    if numero % divisor == 0:
        print('\033[1;33m{}'.format(divisor), end=' ')
        contador += 1
    else:
        print('\033[1;31m{}'.format(divisor), end=' ')

if contador == 2:
    print('\n\033[mO número {} foi divisível 2 vezes e por isso ele é PRIMO!'.format(numero))
else:
    print('\n\033[mO número {} foi divisível {} vezes e por isso ele NÃO É PRIMO!'.format(numero, contador))
    