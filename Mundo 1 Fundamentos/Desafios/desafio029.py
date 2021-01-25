velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.0f}.00!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Sua velocidade de {:.0f}Km/h é menor ou igual ao limite permitido de 80Km/h.'.format(velocidade))