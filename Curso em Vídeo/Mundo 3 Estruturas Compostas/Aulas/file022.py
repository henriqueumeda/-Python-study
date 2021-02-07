valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
'''for valor in valores:
    print(f'{valor}...')'''

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
