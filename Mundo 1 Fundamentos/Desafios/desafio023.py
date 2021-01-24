numero = str(input('Informe um número inteiro entre 1 e 9999: '))
print('Analisando o número {}'.format(numero))
numero = '0000' + numero
digitos = len(numero)
print('Unidade: {}'.format(numero[digitos-1]))
print('Dezena: {}'.format(numero[digitos-2]))
print('Centena: {}'.format(numero[digitos-3]))
print('Milhar: {}'.format(numero[digitos-4]))

#método matemático
num = int(input('Informe um número inteiro entre 1 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
