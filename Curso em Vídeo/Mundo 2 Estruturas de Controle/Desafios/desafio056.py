soma = 0
quantidade_mulheres_menores = 0
idade_homem_maior = 0
velho = ""
for contador in range(1,5):
    print('{:-^19}'.format(' {}ª Pessoa '.format(contador)))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()

    soma += idade

    if sexo in 'Ff' and idade < 20:
        quantidade_mulheres_menores += 1
    elif sexo in 'Mm' and idade > idade_homem_maior:
        velho = nome
        idade_homem_maior = idade

media = soma/4

print('A média de idade do grupo é de {:.1f} anos.'.format(media))

if velho == "":
    print('Não há homens no grupo informado.')
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(idade_homem_maior, velho))

if quantidade_mulheres_menores == 0:
    print('Não há mulheres no grupo informado.')
elif quantidade_mulheres_menores == 1:
    print('Há 1 mulher com menos de 20 anos.')
else:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(quantidade_mulheres_menores))
