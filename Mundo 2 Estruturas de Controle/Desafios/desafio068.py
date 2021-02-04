from random import randint
from unidecode import unidecode

print('-=' * 15)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('-=' * 15)
vitorias = 0

while True:
    numero_user = int(input('Digite um valor inteiro: '))
    numero_pc = randint(0, 11)
    soma = numero_user + numero_pc
    while True:
        opcao_user = input('Par ou Ímpar? [P/I] ').strip().upper()
        if opcao_user == 'P' or opcao_user == 'I':
            break
    if soma % 2 == 0:
        par_impar = 'PAR'
    else:
        par_impar = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {numero_user} e o computador {numero_pc}. Total de {soma} deu {par_impar}')
    print('-' * 30)
    if opcao_user[0] == unidecode(par_impar[0]):
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 15)
        vitorias += 1
    else:
        print('Você PERDEU!')
        print('-=' * 15)
        print(f'GAME OVER! Você venceu {vitorias} vezes!')
        break
