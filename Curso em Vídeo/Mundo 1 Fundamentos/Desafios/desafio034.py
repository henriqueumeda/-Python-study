salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    aumento = 0.1
else:
    aumento = 0.15

print('Quem ganhava \033[1;32mR${:.2f}\033[m passa a ganhar \033[1;32mR${:.2f}\033[m'.format(salario, salario*(1+aumento)))
