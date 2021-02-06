primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
terceiro_numero = int(input('Terceiro número: '))
quarto_numero = int(input('Quarto número: '))

pares = ''
tupla = (primeiro_numero, segundo_numero, terceiro_numero, quarto_numero)
for numero in tupla:
    if numero % 2 == 0:
        pares += str(numero) + ' '

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi inserido')

if pares != '':
    print(f'Os valores pares digitados foram {pares}')
else:
    print(f'Não houveram valores pares')
