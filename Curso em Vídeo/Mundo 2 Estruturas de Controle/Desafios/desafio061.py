print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
numero = primeiro_termo

while contador <= 10:
    print(numero, end=' -> ')
    numero += razao
    contador += 1

print('ACABOU!')