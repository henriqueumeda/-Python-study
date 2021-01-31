from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Serpa que você consegue adivinhar qual foi?''')

numero_user = int(input('Qual é seu palpite? '))
numero_computador = randint(0, 10)
contador = 1

while numero_user != numero_computador:
    if numero_user > numero_computador:
        print('Menos... Tente mais uma vez.')
        contador += 1
    else:
        print('Mais... Tente mais uma vez.')
        contador += 1
    numero_user = int(input('Qual é seu palpite? '))

print('Acertou com {} tentativas. Parabéns!'.format(contador))