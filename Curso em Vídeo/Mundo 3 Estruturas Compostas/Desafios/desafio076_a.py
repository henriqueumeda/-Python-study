lista_preco = (1.75, 2, 15.9, 25, 4.2, 9.99, 120.32, 22.3, 34.9)
lista_objeto = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for contador in range (0, len(lista_objeto)):
    print('{:.<30}R${:>7.2f}'.format(lista_objeto[contador], lista_preco[contador]))
print('-' * 40)
