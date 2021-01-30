from operator import itemgetter
peso = {}

for contador in range(1,6):
    peso[contador] = float(input('Peso da {}ª pessoa: '.format(contador)))

peso_ordenado = dict(sorted(peso.items(), key=itemgetter(1)))

print('O maior peso lido foi de {}Kg'.format(max(peso_ordenado.values())))
print('O menor peso lido foi de {}Kg'.format(min(peso_ordenado.values())))