print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + 9*razao
for contador in range(primeiro_termo, decimo_termo + 1, razao):
    print(contador, end=' -> ')

print('ACABOU')
