numero = {}
soma = 0
pares = ""
for contador in range(1,7):
    numero[contador] = int(input('Digite o {}º número inteiro: '.format(contador)))
    if numero[contador] % 2 == 0:
        soma += numero[contador]
        pares += str(numero[contador]) + ' '

print('Os números pares informados foram: {}'.format(pares))
print('A soma dos números pares inseridos é {}'.format(soma))