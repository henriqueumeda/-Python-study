from random import shuffle
primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')
list = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(list)
print('A ordem de apresentação será\n{}'.format(list))