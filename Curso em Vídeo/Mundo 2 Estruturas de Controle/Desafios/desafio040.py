primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
media = (primeira_nota + segunda_nota)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(primeira_nota, segunda_nota, media))

if media >= 7:
    print('O aluno está \033[1;36mAPROVADO\033[m!')
elif media >= 5:
    print('O aluno está em \033[1;33mRECUPERAÇÃO\033[m!')
else:
    print('O aluno está \033[1;31mREPROVADO\033[m!')