numero = int(input('\033[33mDigite um número inteiro:\033[m '))
print("""Escolha uma das bases para conversão:
[ \033[1;31m1\033[m ] converter para \033[1;31mBINÁRIO\033[m
[ \033[1;35m2\033[m ] converter para \033[1;35mOCTAL\033[m
[ \033[1;36m3\033[m ] converter para \033[1;36mHEXADECIMAL\033[m""")
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} equivale a \033[1;31m{:0b}\033[m na base \033[1;31mBINÁRIA\033[m.'.format(numero, numero))
    print('O número {} equivale a \033[1;31m{}\033[m na base \033[1;31mBINÁRIA\033[m.'.format(numero, bin(numero)[2:] ))
elif opcao == 2:
    print('O número {} equivale a \033[1;35m{:0o}\033[m na base \033[1;35mOCTAL\033[m.'.format(numero, numero))
    print('O número {} equivale a \033[1;35m{}\033[m na base \033[1;35mOCTAL\033[m.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} equivale a \033[1;36m{:0x}\033[m na base \033[1;36mHEXADECIMAL\033[m.'.format(numero, numero))
    print('O número {} equivale a \033[1;36m{}\033[m na base \033[1;36mHEXADECIMAL\033[m.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente.')