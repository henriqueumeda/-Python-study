peso = float(input('Qual é seu peso (Kg)? '))
altura = float(input('Qual é sua altura (m)? '))
imc = peso / altura ** 2
print('O seu IMC vale {:.2f}.'.format(imc))

if imc < 18.5:
    print('Classificação: Abaixo do Peso.')
elif imc < 25:
    print('Classificação: Peso ideal.')
elif imc < 30:
    print('Classificação: Sobrepeso.')
elif imc < 40:
    print('Classificação: Obesidade.')
else:
    print('Classificação: Obesidade mórbida.')