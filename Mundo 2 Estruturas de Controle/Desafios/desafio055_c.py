maior = 0
menor = 0

for contador in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(contador)))

    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso da lista foi {}Kg'.format(maior))
print('O menor peso da lista foi {}Kg'.format(menor))