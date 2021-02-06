lista_palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in lista_palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra.lower()}', end=' ')
