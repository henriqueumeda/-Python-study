print('Gerador de PA')
print('-=' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
contador = 0
novos_termos = 10

while novos_termos != 0:
    total_termos = contador + novos_termos
    while contador < total_termos:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    novos_termos = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total_termos))