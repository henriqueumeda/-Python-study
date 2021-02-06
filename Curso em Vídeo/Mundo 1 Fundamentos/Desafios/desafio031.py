distancia = float(input('Qual é a \033[4;31mdistância\033[m, em Km, da sua viagem? '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('Você está prestes a começar uma viagem de \033[1;30;47m{}Km\033[m.'.format(distancia))
print('E o \033[1;4;32mpreço\033[m da sua passagem será de \033[1;4;30;42mR${:.2f}\033[m'.format(preco))