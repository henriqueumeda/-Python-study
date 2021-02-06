print('\033[1;33m{:=^40}\033[m'.format('LOJAS HENRIQUE'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra de R${:.2f} à vista no dinheiro/cheque recebe 10% de desconto.'.format(preco))
    print('O valor final de sua compra é de R${:.2f}'.format(preco*0.9))
elif opcao == 2:
    print('Sua compra de R${:.2f} à vista no cartão recebe 5% de desconto.'.format(preco))
    print('O valor final de sua compra é de R${:.2f}'.format(preco * 0.95))
elif opcao == 3:
    print('Sua compra de R${:.2f} será paga em 2 parcelas de R${:.2f}'.format(preco,preco/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra de R${:.2f} será paga em {} parcelas com juros de 20%'.format(preco,parcelas))
    print('O valor total a ser pago é de R${:.2f}, sendo cada parcela igual a R${:.2f}'.format(preco*1.2, preco*1.2/parcelas))
else:
    print('Esta opção de pagamento não existe! Tente novamente.')
