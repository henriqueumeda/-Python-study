import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {}, arredondada para cima, é igual {}'.format(num, math.ceil(raiz)))