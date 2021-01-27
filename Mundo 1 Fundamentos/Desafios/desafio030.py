numero = int(input('\033[33mDigite um número inteiro:\033[m '))
if numero % 2 == 0:
    print('O número {} é \033[1;36mPAR\033[m!'.format(numero))
else:
    print('O número {} é \033[1;31mÍMPAR\033[m!'.format(numero))
