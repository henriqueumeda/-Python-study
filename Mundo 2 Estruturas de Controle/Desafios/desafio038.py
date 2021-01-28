primeiro_numero = int(input('Primeiro número inteiro: '))
segundo_numero = int(input('Segundo número inteiro: '))

if primeiro_numero > segundo_numero:
    print('O \033[1;31mprimeiro valor\033[m é \033[1;34mMAIOR\033[m')
elif primeiro_numero < segundo_numero:
    print('O \033[1;31msegundo valor\033[m é \033[1;34mMAIOR\033[m')
else:
    print('\033[1;31mNão existe\033[m valor maior, os dois são \033[1;34mIGUAIS\033[m')