from time import sleep

primeiro_numero = float(input('Primeiro valor: '))
segundo_numero = float(input('Segundo valor: '))
opcao = 0
print('Escolha a operação que deve ser realizada:', end='')

while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = primeiro_numero + segundo_numero
        print('{} + {} = {}'.format(primeiro_numero, segundo_numero, soma))
    elif opcao == 2:
        multiplicacao = primeiro_numero * segundo_numero
        print('{} x {} = {}'.format(primeiro_numero, segundo_numero, multiplicacao))
    elif opcao == 3:
        if primeiro_numero > segundo_numero:
            print('{} > {}'.format(primeiro_numero, segundo_numero))
        elif primeiro_numero < segundo_numero:
            print('{} > {}'.format(segundo_numero, primeiro_numero))
        else:
            print('{} = {}'.format(primeiro_numero, segundo_numero))
    elif opcao == 4:
        print('Informe os números novamente:')
        primeiro_numero = float(input('Primeiro valor: '))
        segundo_numero = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Escolha novamente.')
    print('-=' * 20, end='')
    sleep(1)

print('\nFim do programa! Volte sempre!')