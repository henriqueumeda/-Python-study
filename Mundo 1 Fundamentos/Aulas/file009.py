frase = '   Curso em Vídeo Python   '
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[2][3])

print("""Welcome! Are you completely new to programming?
If not then we presume you will be looking for information
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")