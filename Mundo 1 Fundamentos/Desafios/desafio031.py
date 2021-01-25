distancia = float(input('Qual é a distância, em Km, da sua viagem? '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
print('E o preço da sua passagem será de R${:.2f}'.format(preco))