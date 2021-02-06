while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    tupla_numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                     'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    print(f'Você digitou o número {tupla_numeros[numero]}')

    continuar = ""
    while continuar != 'S' and continuar != 'N':
        continuar = input('Você quer continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break
