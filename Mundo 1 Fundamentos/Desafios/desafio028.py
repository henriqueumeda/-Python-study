from random import randint
from time import sleep
print('-=-' * 20 + '\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n' + '-=-' * 20)
numeroUser = int(input('Em que número pensei? '))
numeroPC = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if numeroUser == numeroPC:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numeroPC, numeroUser))
