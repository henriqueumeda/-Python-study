valor = int(input('Que valor você quer sacar? R$'))

quantidade_50 = valor // 50
quantidade_20 = (valor - quantidade_50*50) // 20
quantidade_10 = (valor - quantidade_50*50 - quantidade_20*20) // 10
quantidade_1 = valor - quantidade_50*50 - quantidade_20*20 - quantidade_10*10

lista = {50: quantidade_50, 20: quantidade_20, 10: quantidade_10, 1: quantidade_1}

for i in lista:
    if lista[i] != 0:
        print(f'Total de {lista[i]} cédulas de R${i:.2f}')
