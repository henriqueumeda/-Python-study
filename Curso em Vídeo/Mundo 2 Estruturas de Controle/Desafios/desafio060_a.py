''' método simples de resolução de cálculo de fatorial
from math import factorial
numero = int(input('Digite um número inteiro: '))
fatorial = factorial(numero)
print('{}! = {}'.format(numero, fatorial))'''
numero = -1
while numero < 0:
    numero = int(input('Digite um número natural: '))

mensagem = str(numero) + '!='
fatorial = 1

if numero > 0:
    while numero != 0:
        if numero == 1:
            mensagem += '1='
        else:
            mensagem += '{}x'.format(numero)
        fatorial *= numero
        numero -= 1
elif numero == 0:
    fatorial = 1

print('{}{}'.format(mensagem, fatorial))