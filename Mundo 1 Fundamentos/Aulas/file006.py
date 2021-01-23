from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}\nA raiz de {} arredondada para baixo é {}'.format(num, raiz, num, floor(raiz)))
