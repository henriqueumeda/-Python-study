nome = 'Henrique'
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'negativo':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format('\033[7;34m', nome, '\033[m'))
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format(cores['negativo'], nome, cores['limpa']))
print('\033[1;30;43mOlá, Mundo!\033[m')