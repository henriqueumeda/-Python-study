from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print('[Ratio] {}, {}, Similaridade: {}'.format('São Paulo', 'São Paul', fuzz.ratio('São Paulo', 'São Paul')))
s1 = 'Belo Horizonte'
s2 = 'B. Horizonte'
print('[Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.ratio(s1, s2)))

"""Letras maiúsculas e minúsculas"""
s1 = 'São Paulo'
s2 = 'são paulo'
print('[Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.ratio(s1, s2)))

"""Pontuação ou outros caracteres influenciam no score"""
s1 = 'São Paulo'
s2 = 'São Paulo!!'
print('[Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.ratio(s1, s2)))

"""Similaridade Parcial
    - Similaridade parcial busca apenas a string em questão e descarta o resto.
    - Extremamente útil para trabalhar com dados coletados da web ou ainda quando queremos ignorar pontuações."""

# Consultando o score usando o método ratio
s1 = 'São Paulo'
s2 = '###$$%$!São Paulo#$#%#ˆˆˆˆˆ!!'
print('[Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.ratio(s1, s2)))

# Consultando o score usando o método partial
s1 = 'São Paulo'
s2 = '###$$%$!São Paulo#$#%#ˆˆˆˆˆ!!'
print('[Partial Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.partial_ratio(s1, s2)))

# Consultando o score usando o método partial
# alteração nas strings
s1 = 'São Paulo'
s2 = '###$$%$!São Paullo#$#%#ˆˆˆˆˆ!!'
print('[Partial Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.partial_ratio(s1, s2)))

"""Ordem de caracteres diferentes?"""
# Consultando o score usando o método partial
# alteração nas strings
s1 = 'São Paulo'
s2 = 'Paulo São'
print('[Partial Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.partial_ratio(s1, s2)))

# - Função partial_token_sort_ratio() separa os tokens por espaço e ordena por ordem alfabética.
# - Coloca as strings em letras minúsculas.
# - Considera apenas as strings consultadas.

# Consultando o score usando o método partial
# alteração nas strings
s1 = 'São Paulo'
s2 = 'Paulo São'
print('[Partial Token Sort Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.partial_token_sort_ratio(s1, s2)))

# Consultando o score usando o método partial
# alteração nas strings
s1 = 'São Paulo'
s2 = 'São Paullo'
print('[Partial Token Sort Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.partial_token_sort_ratio(s1, s2)))

# Consultando o score usando o método partial e com caracteres minusculos.
s1 = 'São Paulo'
s2 = '###$$%$!são paulo#$#%#ˆˆˆˆˆ!!'
print('[Partial Token Sort Ratio] {}, {}, Similaridade: {}'.format(s1, s2, fuzz.partial_token_sort_ratio(s1, s2)))

print()
print('-' * 100)
print()

"""Processando uma Lista de Strings
    - Aplicar o fuzzywuzzy para corrigir strings em uma base de dados"""

"""Cria lista de strings"""
lista = ['Doença Cardiovascular.','doença cardiovascular!!', 'Doenca Cardiovascular', 'Doenc. Cardio']

"""Extrai os scores de similaridades com uma string em questão"""
print('[Partial Ratio] ', process.extract('Doença Cardiovascular', lista, scorer=fuzz.partial_ratio))

"""Limitando o retorno"""
print('[Partial Ratio] Top 2: ', process.extract('Doença Cardiovascular', lista, scorer=fuzz.partial_ratio, limit=2))

"""Retorna apenas uma string com um score acima de 95"""
print('[Partial Ratio] Top 1 (Score >= 95): ', process.extractOne('Doença Cardiovascular', lista, scorer=fuzz.partial_ratio, score_cutoff=95))

"""Data Cleaning em um DataFrame
     - Aplicar o fuzzywuzzy em uma base de dados
     - Medir a similaridade de strings e fazer Data Cleaning"""

print()
print('-' * 100)
print()

import pandas as pd
from collections import OrderedDict
data = OrderedDict(
    {
        'descrição': ['São Paulo', 'SãoPaulo', 'São Pauloo','São Paulo,,', 'Belo Horizonte', 'B. Horizonte']
    })

"""Converte Dicionário para Pandas Dataframe"""
df = pd.DataFrame(data)

"""Corrigindo dados do dataframe"""
lista_cidades = ['Belo Horizonte', 'São Paulo']

for cidade in lista_cidades:
    for i in df.descrição.items():
        print('[Partial Token Sort Ratio] {}, {}, Similaridade: {}'.format(cidade, i[1], fuzz.partial_token_sort_ratio(cidade, i)))

print()
print('-' * 100)
print()

print(df)

print()
print('-' * 100)
print()

"""Atualizando as linhas do Dataframe se similaridade for maior que um determinado valor"""
for cidade in lista_cidades:
    for i in df.descrição.items():
        print('[Partial Token Sort Ratio] {}, {}, Similaridade: {}'.format(cidade, i[1], fuzz.partial_token_sort_ratio(cidade, i)))
        if fuzz.partial_token_sort_ratio(cidade, i[1]) >= 70:
            df.loc[df['descrição'] == i[1], ['descrição']] = cidade

print()
print('-' * 100)
print()

print(df)
