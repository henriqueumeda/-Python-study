lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[::-1])
print(lanche[-3:])
print(sorted(lanche))
print(lanche)
# Tuplas são imutáveis
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-' * 30)

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

print('-' * 30)

for posicao, alimento in enumerate(lanche):
    print(f'Eu vou comer {alimento} na posicao {posicao}')
