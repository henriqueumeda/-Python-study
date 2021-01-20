reais = float(input('Digite o valor total na sua carteira: R$'))
dolar = reais / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(reais, dolar))