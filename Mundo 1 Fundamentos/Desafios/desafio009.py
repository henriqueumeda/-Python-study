numero = int(input('Digite um número inteiro: '))
mensagem = 'A tabuada do número {} é: \n'

for i in range(1,10):
    resultado = numero * i
    mensagem = mensagem + str(numero) + 'x' + str(i) + '=' + str(resultado) + '\n'

print(mensagem.format(numero))