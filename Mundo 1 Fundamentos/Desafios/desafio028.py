from random import randint
from time import sleep
print('\033[33m-=-' * 20 + '\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n' + '-=-' * 20 + '\033[m')
numeroUser = int(input('Em que número pensei? '))
numeroPC = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if numeroUser == numeroPC:
    print('\033[1;36mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('\033[1;31mGANHEI!\033[m Eu pensei no número \033[1;4;31m{}\033[m e não no \033[1;37m{}\033[m!'.format(numeroPC, numeroUser))
