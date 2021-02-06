nome = str(input('Digite o seu nome completo: ')).strip()
nomeDividido = nome.split()
nomeJunto = ''.join(nomeDividido)

print("""Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras""".format(nome.upper(), nome.lower(), len(nomeJunto), nomeDividido[0], len(nomeDividido[0])))