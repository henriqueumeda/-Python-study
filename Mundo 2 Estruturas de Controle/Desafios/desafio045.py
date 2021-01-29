from random import randint
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao_user = int(input('Qual é a sua jogada? '))
opcao_computador = randint(0, 2)
lista_opcoes = ('PEDRA','PAPEL','TESOURA')
if opcao_user > 2:
    print('OPÇÃO INVÁLIDA!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 13)
    print('Computador jogou {}'.format(lista_opcoes[opcao_computador]))
    print('Jogador jogou {}'.format(lista_opcoes[opcao_user]))
    print('-=' * 13)
    if opcao_user == opcao_computador:
        print('EMPATE')
    elif (opcao_user == 0 and opcao_computador == 2) or (opcao_user == 1 and opcao_computador == 0) or (opcao_user == 2 and opcao_computador == 1):
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')


