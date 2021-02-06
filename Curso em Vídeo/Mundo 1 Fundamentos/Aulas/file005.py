import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual {:.2f}\nA raiz de {} arredondada para cima é {}'.format(num, raiz, num, math.ceil(raiz)))