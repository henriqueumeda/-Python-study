from datetime import date

ano_nascimento = int(input('Insira o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano_nascimento + 18))
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano_nascimento + 18))
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
    print('Você deve se alistar IMEDIATAMENTE!')