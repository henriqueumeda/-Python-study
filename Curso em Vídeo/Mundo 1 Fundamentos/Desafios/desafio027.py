nome = input('Digite seu nome completo: ')
listaNomes = nome.split()
print("""Muito prazer em te conhecer!
Seu primeiro nome é {}
Seu último nome é {}""".format(listaNomes[0], listaNomes[len(listaNomes)-1]))
