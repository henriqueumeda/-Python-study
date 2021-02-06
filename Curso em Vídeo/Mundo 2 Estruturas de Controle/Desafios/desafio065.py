sim_nao = "S"
soma = contador = maior = menor = 0

while sim_nao not in 'Nn':
    numero = int(input('Digite um número inteiro: '))
    sim_nao = input('Quer continuar? [S/N] ')
    soma += numero
    contador += 1

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma/contador

print('Você digitou {} números e a média foi {:.2f}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))