from datetime import date
ano_atual = date.today().year
ano_nascimento = {}
idade = {}
maiores = 0
menores = 0

for contador in range(1,8):
    ano_nascimento[contador] = int(input('Em que ano a {}ª pessoa nasceu? '.format(contador)))

    if ano_nascimento[contador] > ano_atual:
        print('[ERRO] Esta pessoa ainda não nasceu!')
    else:
        idade[contador] = ano_atual - ano_nascimento[contador]

        if idade[contador] >= 18:
            maiores += 1
        else:
            menores += 1

print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} menos de idade'.format(maiores, menores))
