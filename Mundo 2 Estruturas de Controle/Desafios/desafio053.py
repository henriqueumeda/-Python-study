frase = input('Digite uma frase: ').upper().strip().replace(' ', '')
tamanho = int(len(frase))
inverso = ''

#Opção mais simples:
# inverso = frase[::-1]

for contador in range(tamanho-1, -1, -1):
    inverso += frase[contador]

print('O inverso de {} é {}'.format(frase, inverso))

if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')