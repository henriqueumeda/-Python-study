valor_total = produtos_maiores_1000 = produto_mais_barato = preco_mais_barato = 0

while True:
    produto = input('Nome do produto: ')
    preco = 0
    while preco <= 0:
        preco = float(input('Preço: R$'))

    if valor_total == 0 or preco < preco_mais_barato:
        produto_mais_barato = produto
        preco_mais_barato = preco

    if preco > 1000:
        produtos_maiores_1000 += 1

    valor_total += preco

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer continuar [S/N]? ').strip().upper()[0]

    if continuar == 'N':
        break

print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'Total da compra: R${valor_total:.2f}')
print(f'Produtos custando mais que R$1000.00: {produtos_maiores_1000}')
print(f'Produto mais barato: {produto_mais_barato} -> Preço: R${preco_mais_barato:.2f}')