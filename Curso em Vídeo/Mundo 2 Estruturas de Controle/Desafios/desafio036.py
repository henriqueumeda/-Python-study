valor = float(input('Qual o \033[4mvalor da casa\033[m a ser comprada? R$'))
salario = float(input('Qual é o seu \033[4msalário\033[m? R$'))
anos = int(input('Em \033[4mquantos anos\033[m você irá pagar a casa? '))
meses = anos * 12
prestacao = valor/meses

if prestacao > 0.3*salario:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
    print("""O valor da prestação mensal de \033[1;32mR${:.2f}\033[m representa mais do que 30% do salário 
    de \033[1;32mR${:.2f}\033[m.""".format(prestacao, salario))
    print('O \033[4mlimite\033[m do valor da prestação mensal é de \033[1;32mR${:.2f}\033[m.'.format(salario*0.3))
else:
    print('\033[1;36mEMPRÉSTIMO APROVADO!\033[m')
    print('O valor da prestação mensal será de \033[1;32mR${:.2f}\033[m'.format(prestacao))
