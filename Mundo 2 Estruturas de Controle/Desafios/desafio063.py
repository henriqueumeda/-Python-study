print('-' * 30)
print('{:^30}'.format('Sequência de Fibonacci'))
print('-' * 30)
quantidade = int(input('Quantos termos você quer mostrar? '))
print('~' * 30)

lista = [0, 1]
contador = 1

while contador <= quantidade:
    if quantidade >= 3 and contador >= 3:
        termo = lista[contador-2] + lista[contador-3]
        lista += [termo]
    print(lista[contador - 1], end=' -> ')
    contador += 1

print('FIM')
print('~' * 30)
