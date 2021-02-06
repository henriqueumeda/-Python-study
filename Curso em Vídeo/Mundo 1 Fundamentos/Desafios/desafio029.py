velocidade = float(input('\033[4;34;40mQual é a velocidade atual do carro?\033[m '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('\033[1;31mMULTADO!\033[m Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de \033[1;4;32mR${:.0f}.00\033[m!'.format(multa))
else:
    print('\033[35mTenha um bom dia! Dirija com segurança!\033[m')