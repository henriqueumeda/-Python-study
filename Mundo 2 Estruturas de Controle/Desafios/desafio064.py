numero = contador = soma = 0

while numero != 999:
    numero = int(input('Digite um número inteiro [999 para parar]: '))

    if numero != 999:
        soma += numero
        contador += 1

print('Você digitou {} números e a soma deles foi {}'.format(contador, soma))