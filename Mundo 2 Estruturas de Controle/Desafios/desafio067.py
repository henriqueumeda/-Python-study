while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if numero < 0:
        break
    for contador in range(1,11):
        multiplicacao = numero*contador
        print(f'{numero} x {contador} = {multiplicacao}')
    print('-' * 30)

print('Programa de tabuada encerrado! Volte sempre!')