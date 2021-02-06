cidade = input('Em que cidade você nasceu? ')
primeiroNome = cidade.replace('-', ' ').split()[0].capitalize()
print(primeiroNome)
print('O primeiro nome da sua cidade é "Santo"? {}'.format(primeiroNome == "Santo"))
