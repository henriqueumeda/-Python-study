classificacao_brasileirao = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense',
                             'Palmeiras', 'Grêmio', 'Corinthians', 'Bragantino', 'Atlético-PR',
                             'Santos', 'Ceará SC', 'Atlético-GO', 'Sport Recife', 'Fortaleza',
                             'Vasco', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {classificacao_brasileirao}')
print('-=' * 15)
print(f'Os 5 primeiros são {classificacao_brasileirao[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {classificacao_brasileirao[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(classificacao_brasileirao)}')
print('-=' * 15)
print(f'O Vasco está na {classificacao_brasileirao.index("Vasco")+1}ª posição')