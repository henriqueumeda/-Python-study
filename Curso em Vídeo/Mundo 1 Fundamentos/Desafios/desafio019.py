from random import choice
primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')
choiceList = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
print('O aluno escolhido foi {}'.format(choice(choiceList)))