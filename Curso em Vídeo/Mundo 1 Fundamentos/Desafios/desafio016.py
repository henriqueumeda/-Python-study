from math import floor, trunc
numero = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, int(numero)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, floor(numero)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, trunc(numero)))