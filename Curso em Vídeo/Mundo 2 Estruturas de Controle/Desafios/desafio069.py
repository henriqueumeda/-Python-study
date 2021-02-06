pessoas_maiores_idade = 0
homens = 0
mulheres_menos_20_anos = 0

while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))

    if idade > 18:
        pessoas_maiores_idade += 1

    sexo = ""
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    print('-' * 30)

    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres_menos_20_anos += 1

    continuar = ""
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break

print(f"""Total de pessoas com mais de 18 anos: {pessoas_maiores_idade}
Homens cadastrados: {homens}
Mulheres com menos de 20 anos: {mulheres_menos_20_anos}""")