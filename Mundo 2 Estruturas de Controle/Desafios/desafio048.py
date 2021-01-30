soma = 0
contador = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        contador += 1
        soma += numero

print('A soma dos {} números ímpares múltiplos de 3, no intervalo de 1 a 500, vale {}'.format(contador, soma))
